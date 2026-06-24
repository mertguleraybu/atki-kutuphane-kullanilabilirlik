import streamlit as st

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
st.sidebar.title("Menü")
page = st.sidebar.radio(
    "Sayfa seç:",
    ["ATKI Hesaplayıcı", "README / Metodoloji"]
)

# -----------------------------
# SAYFA 1: HESAPLAYICI
# -----------------------------
if page == "ATKI Hesaplayıcı":

    st.title("Ajan Temelli Kullanılabilirlik İndeksi (ATKI)")

    st.markdown("### Girdi Değerleri")

    dgb = st.slider("DGB (Doğrulanmış Görev Başarısı)", 0.0, 1.0, 1.0)
    kgp = st.slider("KGP (Kanıt Geçerlilik Puanı)", 0.0, 1.0, 1.0)
    ho = st.slider("HO (Hata Oranı)", 0.0, 5.0, 0.1)

    gs = st.number_input("GS (Gereksiz Sapma)", 0)
    ki = st.number_input("KI (Kısıt İhlali)", 0)
    gk = st.number_input("GK (Görevden Kopma)", 0)
    ta = st.number_input("TA (Toplam Adım)", min_value=1, value=10)

    ajan = st.slider("Ajan Puanı", 0, 100, 80)

    # Hesaplama
    sso = max(0, 1 - ((gs + ki + gk) / ta))
    atki = 100 * (0.25*dgb + 0.25*kgp + 0.25*(1-ho) + 0.25*sso)
    sapma = ajan - atki

    st.markdown("### Sonuçlar")

    st.metric("SSO (Semantik Sürtünme Oranı)", round(sso, 3))
    st.metric("ATKI Skoru", round(atki, 2))
    st.metric("Simüle Edilmiş Başarı Sapması", round(sapma, 2))

    # Basit grafik
    st.markdown("### Görsel Karşılaştırma")
    st.bar_chart({
        "Skorlar": [atki, ajan]
    })

# -----------------------------
# SAYFA 2: README
# -----------------------------
elif page == "README / Metodoloji":

    st.title("Metodoloji ve Açıklamalar")

    st.markdown("""
## 📌 Ajan Temelli Kullanılabilirlik İndeksi (ATKİ)

ATKI, otonom ajanların bir web sitesinde görevleri ne kadar **doğru, kanıtlanabilir ve tutarlı** tamamladığını ölçmek için geliştirilmiştir.

---

## 🧮 Formül

ATKI = 100 × [0.25(DGB) + 0.25(KGP) + 0.25(1 − HO) + 0.25(SSO)]

---

## 🔍 Bileşenler

### 🔹 DGB — Doğrulanmış Görev Başarısı
- 1 → Görev doğru
- 0 → Görev yanlış

---

### 🔹 KGP — Kanıt Geçerlilik Puanı
- 1 → Doğru ve erişilebilir kanıt
- 0.5 → Kısmen doğru
- 0 → Yanlış / uydurma

---

### 🔹 HO — Hata Oranı
HO = Hata sayısı / Toplam adım

- Yüksek HO → kötü performans

---

### 🔹 SSO — Semantik Sürtünme Oranı

SSO = 1 − (GS + KI + GK) / TA

#### Bileşenler:
- GS → Gereksiz sapma
- KI → Kısıt ihlali
- GK → Görevden kopma
- TA → Toplam adım

---

## 📉 Ek Metrik

Simüle Edilmiş Başarı Sapması:

Sapma = Ajan Puanı − ATKI

👉 Büyük fark = model aşırı özgüvenli / halüsinatif

---

## 🎯 Yorum

Bu indeks:
- Sadece sonucu değil
- Süreci ve doğrulanabilirliği de ölçer

👉 Yani klasik kullanılabilirlikten farklıdır.

---

## ⚠️ Akademik Not

Bu model:
- Saf site performansı ölçmez
- Saf model performansı da ölçmez

👉 **Ajan + sistem etkileşimini ölçer**
""")