# Logs - Ham Oturum Verileri Arşivi

Bu klasör, tezin deneysel aşamasında LLaMA 3 ve Mistral 7B otonom ajanları tarafından gerçekleştirilen tüm test oturumlarına ait kronolojik ham log kayıtlarını barındırmaktadır. Deneyler kapsamında 2 farklı model, 11 farklı sorgu senaryosu ve her senaryo için 5 tekrarlı bağımsız oturum yürütülmüştür. Bu doğrultuda veri kümesinde toplam 110 adet bağımsız oturuma ait tam gezinme ve akıl yürütme adımları yer almaktadır.

---

## Klasör Yapısı

Klasör içindeki veriler, modellerin performanslarını ve operasyonel davranışlarını ayrı ayrı denetlemeyi kolaylaştırmak amacıyla iki alt dizine ayrılmıştır:

* **Llama3**: LLaMA 3 modeliyle yürütülen 55 bağımsız oturumdan elde edilen ham log kayıtlarını barındırır. Her bir oturumun tarayıcı adımları, model kararları ve semantik rotaları hem düzenlenebilir DOCX formatında hem de arşivlenebilir PDF formatında saklanmaktadır.
* **Mistral**: Mistral 7B modeliyle yürütülen 55 bağımsız oturumdan elde edilen ham log kayıtlarını barındırır. Modelin test senaryolarındaki tüm eylemleri, zaman damgalı gezinme verileri ve çıktıları hem DOCX hem de PDF formatlarında mevcuttur.

---

## Log Verilerinin Yapısı ve İçerik Düzeni

Her bir log dosyası, otonom ajanın Cumhurbaşkanlığı Millet Kütüphanesi (https://www.mk.gov.tr) web sitesinde gerçekleştirdiği operasyonları uçtan uca takip edebilmeyi sağlayan standart bir akış mimarisine sahiptir. Dosyaların içerisinde şu ana bileşenler yer almaktadır:

1. **Oturum ve Görev Bilgileri**: Test edilen modelin adı, deneme numarası ve ajana prompts.py üzerinden iletilen doğal dildeki hedef görevin tam metni.
2. **Adım Adım Gezinme Kayıtları**: Ajanın Playwright tarayıcısı üzerinden gerçekleştirdiği her bir tıklama, form doldurma veya sayfa geçiş eyleminin kronolojik dökümü.
3. **Akıl Yürütme ve Karar Metinleri**: Ajanın ReAct döngüsü uyarınca, karşılaştığı HTML sayfa yapısına yönelik ürettiği iç düşünceler, gözlemler ve bir sonraki adıma geçiş kararları.
4. **Nihai Çıktı ve Öz Değerlendirme**: Görev tamamlandığında veya durma sınırına ulaşıldığında ajanın kullanıcıya sunduğu nihai yanıt ve kendi performansına verdiği Ajan Puanı.

---

## Analiz ve Doğrulama Amacı

Bu ham kayıtlar, projenin Results klasöründe yer alan kodlama matrisindeki nicel verilerin kaynak dokümanları niteliğindedir. Araştırmacılar bu logları inceleyerek; ajanların hangi web bileşenlerinde takıldığını, hangi noktalarda kısıt ihlali yaparak alan adı dışına çıktığını, hangi aşamalarda halüsinasyon ürettiğini ve Simüle Edilmiş Başarı Sapması değerlerinin arka planındaki nitel gerekçeleri doğrudan doğrulayabilirler.