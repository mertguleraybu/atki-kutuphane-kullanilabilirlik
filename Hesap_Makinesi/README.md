# Calculator - ATKİ Hesap Makinesi ve Metodoloji Arayüzü

Bu klasör, tez çalışmasında geliştirilen Ajan Temelli Kullanılabilirlik İndeksi (ATKİ) formülünün pratik, etkileşimli ve görsel bir şekilde hesaplanabilmesi amacıyla geliştirilmiş Streamlit tabanlı web arayüzü uygulamasını barındırmaktadır. Hesap makinesi, kullanıcıların otonom ajan oturumlarından elde ettikleri ham değişken verilerini girerek ATKİ skorunu, Semantik Sistem Uyumu (SSO) değerini ve Simüle Edilmiş Başarı Sapması (SEBS) farkını anlık olarak grafiksel raporlarla hesaplamasını sağlar.

---

## Bağımlılıklar ve Kurulum

Bu uygulamanın çalışabilmesi için sisteminizde Python 3.x ve klasör içinde tanımlanan bağımlılıkların kurulu olması gerekmektedir.

1. Terminalinizde `Calculator/` dizinine geçiş yapın:
cd Calculator

2. İlgili kütüphaneleri (Streamlit ve bağımlılıkları) yükleyin:
pip install -r requirements.txt

---

## Uygulamayı Çalıştırma

Kurulum tamamlandıktan sonra yerel sunucuda arayüzü başlatmak için aşağıdaki komutu koşturun:
streamlit run ATKI_streamlit_calculator.py

Komut çalıştırıldıktan sonra tarayıcınızda otomatik olarak http://localhost:8501 adresi açılacaktır.

---

## Arayüz Özellikleri ve Kullanım Kılavuzu

Uygulama, Streamlit sol menüsü üzerinden geçiş yapılabilen iki ana sayfadan oluşmaktadır:

### 1. ATKİ Hesaplayıcı Sayfası
Bu sayfada, bir ajan test oturumuna ait nicel veriler girilerek performans analizi yapılır. Giriş alanları arasında Doğrulanmış Görev Başarısı (DGB) ve Kanıt Geçerlilik Puanı (KGP) için 0.0 - 1.0 arası kaydırma çubukları bulunur. Hata Oranı (HO) için 0.0 - 5.0 arası hassas değer seçici mevcuttur. Gereksiz Sapma (GS), Kısıt İhlali (Kİ), Görevden Kopma (GK) sayısal tam sayı girdileri ve Toplam Adım (TA) bilgisi girilebilmektedir. Ajanın görev sonunda kendi performansına verdiği 0 - 100 arası Ajan Puanı (AP) da bu sayfada tanımlanır. Sistem girdi değerlerine bağlı olarak Semantik Sistem Uyumu (SSO) yüzdesini, ATKİ Skorunu ve Simüle Edilmiş Başarı Sapmasını (SEBS) anlık hesaplar ve dinamik bir sütun grafiği ile raporlar.

### 2. Metodoloji Sayfası
Hesaplama mantığının teorik arka planını içeren rehber sayfadır. ATKİ bileşik indeks formülünün matematiksel detaylarını gösterir ve tüm metriklerin tezin metodolojisindeki karşılıklarını ve puanlama kurallarını listeler.

---

## Dosya Yapısı

* **ATKI_streamlit_calculator.py**: Giriş kontrollerini, matematiksel arka plan hesaplamalarını ve grafik arayüz bileşenlerini içeren ana Streamlit kaynak kodudur.
* **requirements.txt**: Uygulamanın çalışması için gerekli olan streamlit ve ilgili veri işleme kütüphanelerinin tam sürümlerini içeren bağımlılık listesidir.