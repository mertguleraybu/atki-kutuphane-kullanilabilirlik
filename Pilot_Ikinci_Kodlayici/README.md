# Pilot İkinci Kodlayıcı Güvenilirlik Denetimi

Bu dizin, kütüphane web sitelerinde ajan temelli kullanılabilirliğin ölçümü araştırması kapsamında gerçekleştirilen pilot ikinci kodlayıcı kontrolü çalışmalarını, veri setini ve uygulama protokollerini içermektedir. Yapılan çalışma insan ikinci kodlayıcı yerine geçmemekte olup, tez öncesi süreçte kodlama kararlarının izlenebilirliğini ve pilot güvenilirliğini denetlemek amacıyla kurgulanmıştır.

## Araştırma Kapsamı ve Örneklem Seçimi

Güvenilirlik denetimi için veri setinde yer alan toplam 110 oturum arasından tabakalı örnekleme yöntemi kullanılmıştır. En dengeli dağılımı sağlamak adına her yapay zekâ modeli ve her görev uygulamasından birer oturum seçilerek Deneme 3 verileri analiz edilmiştir. Bu doğrultuda toplam 22 oturum ve bu oturumlar üzerinden verilen 88 bağımsız karar denetim kapsamına alınmıştır. Denetim sürecinde kör kodlama ilkesi benimsenmiş olup ikinci kodlayıcıya bir önceki kodlama puanları gösterilmemiş, yalnızca görev metinleri, altın standartlar ve ilgili ham log kayıtları sunulmuştur.

## Kodlama Alanları ve Karar Kuralları

Denetim sürecinde değerlendirilen değişkenler belirli kurallara göre şekillendirilmiştir. Doğru Görev Başarımı (DGB) değişkeni sistemin doğru nihai sonuca ulaşıp ulaşmadığını test ederken, Kanıt Geçerliliği Puanı (KGP) sağlanan URL adresinin geçerli ve görevi destekler nitelikte olup olmadığını inceler. Hata Durumu değişkeni sistemde görevin temel amacını bozan kritik bir hatanın varlığını ölçerken, Semantik Sistem Uyumu (SSO) kategorisi ise sistemin görev çizgisinde kalma düzeyini belirlemektedir. Güvenilirliği artırmak adına SSO verileri sürekli değer yerine düşük, orta ve yüksek olmak üzere kategorik olarak ele alınmıştır.

## Uyum Bulguları ve İstatistiki Değerlendirme

Yapılan pilot denetim sonucunda 22 oturum ve 88 karar üzerinden genel yüzde uyum oranı 0.852 (yüzde 85.2) olarak hesaplanmıştır. Değişken bazlı uyum düzeyleri ve istatistikleri şu şekildedir:

Doğru Görev Başarımı (DGB) değişkeninde yüzde uyum 0.864 ve Cohen kappa değeri 0.593 olarak bulunmuş olup uyum düzeyi iyi olarak yorumlanmıştır.

Kanıt Geçerliliği Puanı (KGP) değişkeninde yüzde uyum 0.864 ve Cohen kappa değeri 0.359 olarak gerçekleşmiş, bu durum iyi uyum olarak değerlendirilmiştir.

Hata Var/Yok kararında yüzde uyum 1.000 ve Cohen kappa değeri 1.000 ile çok iyi düzeyde tam uyum sergilemiştir.

Semantik Sistem Uyumu (SSO) kategorisinde ise yüzde uyum 0.682 ve Cohen kappa değeri 0.516 ile orta düzeyde bir uyum göstermiştir.

## Bulguların Yorumlanması ve Uygulama Notları

Araştırmada başlıca uyumsuzlukların KGP ve SSO kararlarında yoğunlaştığı görülmüştür. Kanıt URL geçerliliği ile semantik uyum sınırlarında kodlayıcıların kişisel yorumlarının daha etkili olduğu anlaşılmıştır. Yüzde 80 ve üzerindeki genel pilot uyum düzeyi kabul edilebilir sınırda yer almaktadır. Semantik uyum değerlendirmelerinde ortaya çıkan yorum farklarını azaltmak amacıyla karar kurallarının daraltılması ve tartışmalı oturumların yeniden gözden geçirilmesi önerilmektedir. Bu dosyalarda sunulan değerler bir pilot yapay zekâ denetimi niteliği taşımaktadır. İlerleyen aşamalarda insan ikinci kodlayıcı uygulaması yapıldığında da aynı metodolojik altyapı kullanılabilecek olup, tez metninde asıl insan kodlayıcı uyum değerleri raporlanmalıdır.
