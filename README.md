# Kütüphane Web Sitelerinde Ajan Temelli Kullanılabilirlik Ölçümü

Bu depo, büyük dil modeli (LLM) tabanlı otonom yapay zekâ ajanlarının web sitelerindeki kullanılabilirlik ve bilgi mimarisi performansını ölçmek amacıyla yürütülen "Kütüphane Web Sitelerinde Ajan Temelli Kullanılabilirliğin Ölçümü: Cumhurbaşkanlığı Millet Kütüphanesi Örneği" başlıklı yüksek lisans tez projesinin kaynak kodlarını, test araçlarını, ham log verilerini ve analiz sonuçlarını içermektedir.

Çalışma kapsamında geliştirilen Ajan Temelli Kullanılabilirlik İndeksi (ATKİ) ölçüm modeli; Doğrulanmış Görev Başarısı (DGB), Kanıt Geçerliliği Puanı (KGP), Hata Oranı (HO) ve Semantik Sistem Uyumu (SSO) olmak üzere dört temel bileşenden oluşmaktadır. Deneyler, yerel altyapıda koşturulan LLaMA 3 ve Mistral 7B modelleri üzerinden toplam 110 bağımsız oturum senaryosu ile gerçekleştirilmiştir.

---

## Proje Klasör Yapısı

Depo içerisindeki dosyalar, test süreçleri ve analiz aşamalarına göre aşağıdaki hiyerarşide düzenlenmiştir:

* **Agent/**: Web ajanının çalışmasını sağlayan Playwright tabanlı Python (.py) kaynak kodlarını ve gerekli bağımlılıkları içeren `Requirements.txt` dosyasını barındırır.
* **Calculator/**: Projede geliştirilen ATKİ formülünün hesaplanmasını kolaylaştırmak amacıyla Streamlit kütüphanesiyle yazılmış hesap makinesi uygulamasını, uygulamaya ait `Requirements.txt` bağımlılık listesini ve detaylı kullanım kılavuzunu içeren özel bir `Readme.md` dosyasını barındırır.
* **Logs/**: Deney oturumlarına ait tüm ham verileri içeren ana arşiv klasörüdür. Klasörün yapısını ve log okuma detaylarını açıklayan bir `Readme.md` dosyası ile birlikte alt iki klasörden oluşur:
    * **Llama3/**: LLaMA 3 modeliyle yürütülen 55 bağımsız oturumdan elde edilen ham log kayıtlarının DOCX ve PDF formatındaki hallerini içerir.
    * **Mistral/**: Mistral 7B modeliyle yürütülen 55 bağımsız oturumdan elde edilen ham log kayıtlarının DOCX ve PDF formatındaki hallerini içerir.
* **Results/**: Oturum verilerinin kodlanması ve formül çıktılarının alınmasıyla üretilen nihai ATKİ puan sonuçlarını, veri matrislerini ve analiz dosyalarını XLSX (Excel) ve PDF formatlarında barındırır.

---

## Matematiksel Model ve ATKİ Formülü

Ajanların web arayüzleri üzerindeki kullanılabilirlik düzeyini hesaplayan bileşik indeks formülü şu şekildedir:

$$ATKİ = 100 \times [0,25 \times DGB + 0,25 \times KGP + 0,25 \times (1 - HO) + 0,25 \times SSO]$$

Formülde yer alan Semantik Sistem Uyumu (SSO) bileşeni ise ajanın rota verimliliğini şu alt formülle ölçmektedir:

$$SSO = 1 - \frac{GS + Kİ + GK}{TA}$$

### Metrik Tanımları ve Kısaltmalar

* **DGB (Doğrulanmış Görev Başarısı):** Ajanın ürettiği nihai cevabın hedef kurumsal bilgiyle ve altın standart ölçütleriyle doğrulanma düzeyini (0-1 aralığında) gösterir.
* **KGP (Kanıt Geçerliliği Puanı):** Ajan tarafından sunulan kaynak URL veya kanıt metninin resmi alan adı içinde, erişilebilir ve görevle doğrudan ilişkili olup olmadığını (0-1 aralığında) gösterir.
* **HO (Hata Oranı):** Oturumda gerçekleşen kritik hata sayısının, ilgili görev için tanımlanmış hata fırsatı sayısına bölünmesiyle hesaplanır.
* **SSO (Semantik Sistem Uyumu):** Ajanın görev niyetini koruma ve semantik olarak aynı operasyon hattında kalma düzeyini ifade eder.
* **GS (Gereksiz Sapma):** Görevin çözümüne doğrudan hizmet etmeyen fazladan gezinme veya tıklama adımlarıdır.
* **Kİ (Kısıt İhlali):** Resmi alan adı dışına çıkma, doğrulanamayan bilgi üretme veya açık talimatı çiğneme durumudur.
* **GK (Görevden Kopma):** Ajanın hedef görevle bağının tamamen koparak ilgisiz işlem ya da açıklamalar üretmeye başlamasıdır.
* **TA (Toplam Anlamlı Eylem Adımı):** Oturum boyunca gerçekleştirilen tüm tıklama, sayfa geçişi ve gezinme işlemlerinin toplam sayısıdır.
* **AP (Ajan Öz Puanı):** Ajanın görev sonunda kendi performansına olasılıksal olarak verdiği 1-100 arası başarı beyanıdır.
* **SEBS (Simüle Edilmiş Başarı Sapması):** Ajanın kendi çıktısına duyduğu yersiz güveni ölçmek amacıyla hesaplanan fark değeridir ($AP - ATKİ$).

---

## Öne Çıkan Bulgular ve Tasarım Tanısı

Araştırma sonucunda elde edilen bulgular, otonom ajanların geleneksel web arayüzlerinde ciddi semantik sürtünmeler yaşadığını ortaya koymuştur. LLaMA 3 modeli için ortalama ATKİ puanı 38,65 olarak hesaplanırken, Mistral 7B modeli için bu değer 30,23 düzeyinde kalmıştır. 

Ajanların kendi performanslarını değerlendirdikleri öz puanlar (AP) sistematik olarak yüksek çıkmış (ortalama 70-80 bandı), ancak dışarıdan doğrulanan nesnel başarı oranları (DGB) %29,10 seviyesinde kalarak yüksek bir Simüle Edilmiş Başarı Sapması (SEBS) üretmiştir. Bu durum, web sitelerinin yalnızca insan gözü için görsel bir arayüz olarak değil, yapay zekâ ajanları için makinece izlenebilir ve kanıt üretimine elverişli bilgi mimarileri olarak tasarlanması gerektiğini doğrulamaktadır.

---

## Lisans ve Atıf Bilgisi

Bu projede paylaşılan tüm kaynak kodlar ve veri setleri akademik araştırma ve geliştirme faaliyetlerine açıktır. Projedeki verileri veya metodolojiyi çalışmalarınızda kullanmanız durumunda aşağıdaki akademik künyeye atıfta bulunmanız rica olunur:

> Güler, M. M. (2026). Kütüphane Web Sitelerinde Ajan Temelli Kullanılabilirliklerin Ölçümü: Cumhurbaşkanlığı Millet Kütüphanesi Örneği (Yüksek Lisans Tezi). Ankara Yıldırım Beyazıt Üniversitesi, Sosyal Bilimler Enstitüsü, Ankara.