import json
import time
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright
import sys
import random

TARGET = "https://www.mk.gov.tr"
MODELS = ["llama3", "mistral"]
MAX_STEPS = 1

terminal_log = []
json_log = {"session_start": datetime.now().isoformat(), "steps": []}

# --- LOGGER ---
class Logger(object):
    def __init__(self, filename="terminal_log.txt"):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger()

# --- LOG FUNCTION ---
def log(role, message):
    t = datetime.now().strftime("%H:%M:%S")
    line = f"[{t}] [{role}] {message}"
    print(line)
    terminal_log.append(line)

# --- PROMPTS ---
THINK_PROMPT = """
ROL
Sen bir kullanılabilirlik testi katılımcısını taklit eden yapay zekâ ajanısın. Görevin, http://www.mk.gov.tr sitesinde verilen görevleri bir insan gibi gerçekleştirmek. Her adımda sesli düşün.
Davranış Kuralları:
* Her adımda gördüğünü açıkla.
* Kısa ve net cümleler kur.
* Her adımı açık ve tamamlayıcı yaz. Adım eksik olmasın.
* Uzun metin yazma, sayfanın tamamını kopyalama.
* “Next step” ve plan cümleleri kullanma.
* https://www.mk.gov.tr dışına çıkma.
* Görev bitince 1 ile 100 arasında bir başarı puanı ver.
* Adım adım anlatım yok, yalnızca görev sonunda rapor oluştur.
* Cevap verirken sadece task’ı tekrarlama, her alan için gözlem ve mantıksal yorumunu 1-2 cümle ile ver.
"""

ACTION_PROMPT = """
GÖREV: "Millet Kütüphanesi'nin abone olduğu veritabanlarına (e-kaynaklara) uzaktan erişim olanaklarıyla ilgili gönderiyi site üzerinden bulun. 
* Gönderi içeriğinden yola çıkarak kütüphanedeki e-kaynaklara nasıl ulaşılacağını özetleyin. Kanıt URL’sini ve izlenen adımları belirtiniz.
* Görev sonunda kendinizi 1-100 arasında bir kullanıcı deneyimi puanı verin ve bunu rapor edin.

ÇIKTI FORMATI:
Sonuç:
Kanıt URL:
İzlenen adımlar (kısa):
Başarı (1/0)
Not (1-100)
KISIT: Form doldurma yok. Giriş yapma yok. Tahmin yok.
"""

FINAL_REPORT_PROMPT = """
Görevi tamamladın.
Aşağıdaki formatta rapor ver:

Sonuç:
Kanıt URL:
İzlenen adımlar:
Başarı (1/0):
Not (1-100):
"""

# --- LLM ---
def ask_llm(model, prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": True},
        stream=True
    )
    full_text = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            token = data.get("response", "")
            print(token, end="", flush=True)
            full_text += token
    print("\n")
    log(f"LLM:{model}", full_text)
    return full_text.strip()

# --- POPUP ---
def close_popup_if_exists(page):
    selectors = ["text=Kapat","button:has-text('Kapat')","[aria-label='close']"]
    for sel in selectors:
        try:
            btn = page.locator(sel).first
            if btn.is_visible(timeout=1000):
                btn.click(force=True)
                log("SCRIPT", f"Popup kapatıldı ({sel})")
                return True
        except:
            continue
    return False

# --- LINK CLICK ---
def click_best_match(page, target_text):
    try:
        links = page.locator("a")
        for i in range(links.count()):
            link = links.nth(i)
            text = link.inner_text().strip()
            if target_text.lower() in text.lower():
                link.click(force=True)
                page.wait_for_load_state("load", timeout=10000)
                close_popup_if_exists(page)
                log("SCRIPT", f"Tıklandı: {text}")
                return True
        return False
    except Exception as e:
        log("SCRIPT", f"Hata: {e}")
        return False

# --- AGENT ---
def run_agent(model, page):
    log("SYSTEM", f"===== MODEL: {model} =====")

    for step in range(MAX_STEPS):
        close_popup_if_exists(page)

        url = page.url
        title = page.title()
        links = page.eval_on_selector_all("a", "els => els.map(e => e.innerText)")[:15]

        # --- KANIT URL DOĞRULAMA ---
        if "aybu.edu.tr" in url:
            kanit_url = "https://www.aybu.edu.tr/"
        else:
            kanit_url = url

        # --- THINK ---
        think_prompt = f"{THINK_PROMPT}\nURL:{url}\nTITLE:{title}\nLINKS:{links}"
        thoughts = ask_llm(model, think_prompt)

        # --- ACTION ---
        action_prompt = f"{ACTION_PROMPT}\nLINKS:{links}"
        action = ask_llm(model, action_prompt)

        clicked = click_best_match(page, action)

        # --- LOG STEP ---
        json_log["steps"].append({
            "time": datetime.now().isoformat(),
            "model": model,
            "url": url,
            "kanit_url": kanit_url,
            "title": title,
            "think": thoughts,
            "action": action,
            "clicked": clicked
        })

    # --- FINAL REPORT ---
    final_prompt = f"{FINAL_REPORT_PROMPT}\nKanıt URL: {kanit_url}"
    report = ask_llm(model, final_prompt)
    json_log["final"] = report

# --- SAVE ---
def save_logs():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"q4_session_{timestamp}.txt","w",encoding="utf-8") as f:
        f.write("\n".join(terminal_log))
    with open(f"q4_session_{timestamp}.json","w",encoding="utf-8") as f:
        json.dump(json_log,f,indent=2,ensure_ascii=False)

# --- MAIN ---
def main():
    log("SYSTEM", "Agent başlıyor")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            try:
                page.goto(TARGET, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(3000)
            except Exception as e:
                log("ERROR", f"Site açılamadı: {e}")
                sys.exit(1)

            for model in MODELS:
                run_agent(model, page)

            browser.close()

    except Exception as e:
        log("SYSTEM", f"Ana Playwright bloğunda hata: {e}")
        sys.exit(1)

    save_logs()
    log("SYSTEM", "Bitti")

if __name__ == "__main__":
    main()