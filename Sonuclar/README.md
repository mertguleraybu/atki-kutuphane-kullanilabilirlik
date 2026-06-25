# Results - ATKİ Puan Sonuçları ve Veri Matrisleri

Bu klasör, tez çalışması kapsamında LLaMA 3 ve Mistral 7B otonom yapay zekâ ajanlarının test oturumlarından elde edilen nicel analiz sonuçlarını ve ham puan matrislerini barındırmaktadır. Veri setleri, bağımsız oturumların kodlama kararlarını geriye dönük olarak denetleyebilmek amacıyla iki farklı dosya formatında saklanmaktadır.

---

## Klasör İçeriği ve Dosya Formatları

Klasör içerisinde yer alan veri ve analiz dosyaları şu şekildedir:

* **ATKI_Results.xlsx**: 110 bağımsız test oturumunun tamamına ait ham puanlama matrisini içeren ana Excel dosyasıdır. Araştırmacılar bu dosya üzerinden formül girdilerini, değişken bazlı dağılımları ve ham veri satırlarını inceleyebilirler.
* **LLAMA3_Results.pdf**: LLaMA 3 modeliyle gerçekleştirilen test oturumlarının ham puan sonuçlarını, veri bütünlüğünün korunması ve hızlıca incelenebilmesi amacıyla statik olarak arşivlenmiş PDF sürümüdür.
* **Mistral_Results.pdf**: Mistral 7B modeliyle gerçekleştirilen test oturumlarının ham puan sonuçlarını, veri bütünlüğünün korunması ve hızlıca incelenebilmesi amacıyla statik olarak arşivlenmiş PDF sürümüdür.

---

## Ham Veri ve Normalizasyon Detayı

Bu klasörde paylaşılan veri matrisleri, otonom ajanların tarayıcı oturumlarından elde edilen ilk ham puanlama sonuçlarını içermektedir. Bu doğrultuda önemli bir yöntemsel detayın göz önünde bulundurulması gerekmektedir:

1. Bu dosyalardaki veriler üzerinde henüz görev karmaşıklığı veya hata fırsatı sayılarına göre bir performans standardizasyonu ya da normalizasyon işlemi uygulanmamıştır.
2. Tez metninin Bulgular bölümünde yer alan ve 0-100 ölçeğine göre hazırlanan nihai indeks puanları ile hata oranları, bu klasördeki ham oturum verileri üzerinden normalizasyon kurallarına göre yeniden hesaplanarak türetilmiştir.
3. Ham veri dosyasındaki değerlerin doğrudan analize dâhil edilmesi yerine, görevlerin taşıdığı farklı hata fırsatı yüklerinin analitik tutarlılığı korumak adına normalize edilmesi önerilir.

---

## Kodlanan Değişkenler ve Matris Yapısı

Veri matrisinde her bir oturum satırı için şu temel değişkenlerin ham kodlama değerleri yer almaktadır:

* **DGB**: Nihai sonucun görev hedefiyle uyumunu gösteren Doğrulanmış Görev Başarısı ham puanı.
* **KGP**: Sunulan URL veya kanıtın doğrulanabilirliğini gösteren Kanıt Geçerliliği Puanı ham değeri.
* **HS**: Oturum sırasında ajanın gerçekleştirdiği kritik hata sayısı.
* **GS**: Göreve hizmet etmeyen gereksiz sapma adımlarının sayısı.
* **Kİ**: Alan adı dışına çıkma veya doğrulanamayan bilgi üretme gibi kısıt ihlali sayısı.
* **GK**: Ajanın hedef görevle ilişkisinin koptuğu işlem sayısı.
* **TA**: Oturumdaki tüm tıklama ve sayfa geçiş işlemlerini içeren Toplam Anlamlı Eylem Adımı.
* **AP**: Ajanın görev sonunda kendisine verdiği 1-100 arası başarı puanı.