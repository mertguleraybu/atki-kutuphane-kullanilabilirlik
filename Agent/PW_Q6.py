import json
import time
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright
import sys
import random

TARGET = "https://www.mk.gov.tr"
MODELS = ["llama3", "mistral"]
MAX_STEPS = 5

terminal_log = []
json_log = {"session_start": datetime.now().isoformat(), "steps": []}

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

def log(role, message):
    t = datetime.now().strftime("%H:%M:%S")
    line = f"[{t}] [{role}] {message}"
    print(line)
    terminal_log.append(line)

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
GÖREV: Yalnızca Cumhurbaşkanlığı Millet Kütüphanesi’nin resmi web alan adı ve alt alan adları içinde gezin. Kullanıcının hafta sonu otopark kullanımına ilişkin açık ve doğrulanabilir bilgi olup olmadığını belirle.
* Açık ve doğrulanabilir bilgi bulursan bilgiyi kısa biçimde raporla ve kanıt URL ver.
* Böyle bir bilgi bulamazsan YALNIZCA şu sonucu üret: 'Site içinde doğrulanabilir bilgi bulunamadı.' 
* Site dışına çıkma. Doğrulanamayan bilgi üretme. (Tahmin yürütme)

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

def ask_llm(model, prompt):
    response = requests.post("http://localhost:11434/api/generate", json={"model": model, "prompt": prompt, "stream": True}, stream=True)
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

def run_agent(model, page):
    log("SYSTEM", f"===== MODEL: {model} =====")
    for step in range(MAX_STEPS):
        close_popup_if_exists(page)
        url = page.url
        title = page.title()
        links = page.eval_on_selector_all("a", "els => els.map(e => e.innerText)")[:15]
        kanit_url = url

        think_prompt = f"{THINK_PROMPT}\nURL:{url}\nTITLE:{title}\nLINKS:{links}"
        thoughts = ask_llm(model, think_prompt)

        action_prompt = f"{ACTION_PROMPT}\nLINKS:{links}"
        action = ask_llm(model, action_prompt)

        clicked = click_best_match(page, action)

        json_log["steps"].append({"time": datetime.now().isoformat(), "model": model, "url": url, "kanit_url": kanit_url, "title": title, "think": thoughts, "action": action, "clicked": clicked})

    final_prompt = f"{FINAL_REPORT_PROMPT}\nKanıt URL: {kanit_url}"
    report = ask_llm(model, final_prompt)
    json_log["final"] = report

def save_logs():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"q6_session_{timestamp}.txt","w",encoding="utf-8") as f: f.write("\n".join(terminal_log))
    with open(f"q6_session_{timestamp}.json","w",encoding="utf-8") as f: json.dump(json_log,f,indent=2,ensure_ascii=False)

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
            for model in MODELS: run_agent(model, page)
            browser.close()
    except Exception as e:
        log("SYSTEM", f"Hata: {e}")
        sys.exit(1)
    save_logs()
    log("SYSTEM", "Bitti")

if __name__ == "__main__": main()
