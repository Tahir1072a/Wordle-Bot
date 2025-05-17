## Yazılım Geliştirme Projesi Planlama Şablonu

**Proje Adı:** `Wordle Bot`

**Hazırlanma Tarihi:** `17.05.2025`

**Versiyon:** 1.0

---

**1. Proje Özeti**
* **1.1. Projenin Kısa Açıklaması (Elevator Pitch):**
    * Bu projede, 5 harfli kelime oyunu olan wordle oyununu, oyuncuya her hamlede seçebileceği kelime önerisi sunan bir bot entegrasyonu ile yeniden geliştirmeyi amaçlıyorum. Şu anda sadece masaüstü platformda çıkacak şekilde planlanmıştır.
* **1.2. Projenin Amacı:**
    * Bu projeyi geliştirerek hem python yeteneklerimi ileri seviyeye taşımayı hem de information theory'e dayalı, veri analizi yapabilen bir bot geliştirmek istiyorum. Projenin sonunda masaüstünde tam kapsamlı çalışan bir uygulama elde etmek istiyorum.
* **1.3. Hedeflenen Sonuç:**
    * Başarılı şekilde çalışan wordle oyunu ve oyuncuya kelime önerisi sunan veyahut kendi kendine oynayan bir wordle bot'un entegrasyonu.

---

**2. Kapsam ve Hedefler**
* **2.1. Projenin Ana Hedefleri:**
    * `Python dilinde uzmanlaşmak`
    * `Python ile veri tabanı yönetimi ve entegrasyonu yapmak`
    * `PyQT5 gibi modern bir masaüstü geliştirme çerçevesini kullanarak bir masaüstü uygulaması geliştirmek.`
    * `Matematiksel bir temele dayalı kendi kendine karar verebilen bir bot geliştirmek.`
    * `Baştan sona bir uygulama geliştirerek, yazılım geliştirme konusunda (design-pattern) kendimi bir adım öteye taşımak.`
* **2.2. Projenin Kapsamı:**
    * **Neler Dahil?**
        * `Kullanıcı Girişi ve Kayıt modülü geliştirilecek. Veritabanına kullanıcı kayıt ve giriş işlemleri buradan yönetilecek. Model Katmanıdır.`
        * `Database Modülü. Tüm veri tabaını ile ilgili işlevler bu modül aracılığı ile yapılacaktır. Örneğin kullanıcıya özel bilgiler. Oynadığı oyun sayısı, kazandığı kaybettiği oyun oranı vb.`
        * `Wordle Bot Modülü. Wordle bot ile ilgili tüm işlevler bu modül içerisinde tanımlanacaktır.`
        * `Wordle Game Modülü. Oyun ortamı bu modülde kodlancaktır.`
        * `GUI Modülü: Arayüz bileşenleri bu modülde tanımlanacaktır.`
        * `Helper Modülü. Veri toplama, analiz, internet üzerinden kelime listesi çekme vb. işlevler bu modül içerisinde tanımlanacaktır.`
        * `Controller GUI Modülü: Projede MVC yaklaşımı uygulanacaktır ve GUI'da oluşan bir değişikliği Model'a veyahut Model'da oluşan bir değişikliği ise GUI a yansıtacaktır.`
    * **Neler Dahil Değil?**
        * `Bu versiyonda Mobil veya web gibi platformlara çıkmaycaktır.`
        * `Bot için herhangi bir api geliştirilmeyecektir.`
        * `Online olmayacaktır. Sadece kullanıcıya internet üzerinden bir mail gönderme mekanizması eklenecektir.`

---

**3. Temel Özellikler (GitHub Görevleri İçin Temel Oluşturacak)**
* **A. Kullanıcı Yönetimi Özellikleri**
    * **Özellik 1:** Kullanıcı Kayıt İşlemi
        * `Alt Görev/Detay: Kullanıcı adı, e-posta ve şifre bilgilerini alacak bir kayıt formu yapılacak ( GUI Modülü )`
        * `Alt Görev/Detay: Girilen şifrenin tekrar edilmesi, şifreyi doğru girmiş mi? ( GUI Modülü )`
        * `Alt Görev/Detay: Kullanıcı adının kontrolü. Bu ad daha önceden veritabanına kayıtlı mı? `
        * `Alt Görev/Detay: Kullanıcı bilgileri doğru şekilde kontrol edildikten sonra, bilgilerin veri tabanına kaydedilmesi.`
        * `Alt Görev/Detay: Kullanıcıya başarılı\Başarısız durumu hakkında geri bildirim. Ayrıca kullanıcı mailine başarıyla koydolduğuna dair bir mail gönderilecektir.`
    * **Özellik 2:** Kullanıcı Giriş İşlemi
        * `Alt Görev/Detay: Kullanıcı adı (veya e-posta) ve şifre bilgilerini alacak bir giriş formu yapılacak ( GUI Modülü )`
        * `Alt Görev/Detay: Kullanıcının kayıtlı olup olmadığı kontrolü yapılacaktır. Kayıtlı ise uygulamaya girişi sağlanacaktır.`
        * `Alt Görev/Detay: Kullanıcı hatalı bir giriş yaptığında ilgili hata mesajı, kullanıcı ekranına bastırılacaktır. `
    * **Özellik 3:** Kullanıcı Arayüz İşlemleri (Anasayfa)
        * `Alt Görev/Detay: Kullanıcı uygulamaya başarılı bir şekilde giriş yaptığında, yönlendirileceği uygulama anasayfası tasarlanacaktır. Anasayfada Oyna ve Çıkış butonları olacaktır.`
        * `Alt Görev/Detay: Kullanıcı bu anasayfa üzerinden oturumunu sonlandırabilecektir.`
        * `Alt Görev/Detay: Kullanıcı oyna butonu içerisinden direkt uygulamaya yönlendirme yapılacaktır. `

* **B. Wordle Oyun Motorunu Geliştirmek**
    * **Özellik 4:** Wordle arayüzünün oluşturulması
        * `Alt görev/detay: 5 sutün, 6 satırdan oluşan bir grid (ızgara) oluşturulacak. Kullacını grid içerisine klavye üzerinden kelime girebilecek. Enter tuşuna bastığında ise kelime kontrol için ilgili işleve gönderilecek.`
        * `Alt görev/detay: Botun önerdiği ilk 10 kelime ve kelimelerin içerdiği bilgi teorisine dayalı skorları kullanıcıya grid'in yanında gösterilecektir. Her yeni kelime tahmininde burası güncellenecek şekilde dinamik olması gerekiyor.`
        * `Alt görev/detay: Girilen kelime, oyun için izin verilen kelimeler arasında var mı diye kontrol edilecek. Ona göre hata/başarı mesajı gönderilecek`
        * `Alt görev/detay: Aranan kelimeye göre, harflerin konumuyla ilgili kullanıcıya geri bildirim yapılacak. (Konumu doğru ise: yeşil, konumu yanlış ise: sarı, hiçbir konumda yoksa: gri) rengini alacak şekilde grid kutucukları güncellenecek.`
        * `Alt görev/detay: 6 denemede kullanıcı kelimeye ulaşamazsa, ekrana başarısız mesajı basılacak ve doğru kelime gösterilecek. Kullanıcı anasayfaya geri yönlendirilecek.`
        * `Alt görev/detay: Her oyun sonu kullanıcıya ait istatistikler (kaç tahminde buldu, kazandı/kaybetti vb.) veritabanına kaydedilecek.`

* **C. Wordle Bot Geliştirmek**
  * **Özellik 5:** Wordle Bot Algortiması
    * `Alt görev/detay: sadasf`

---

**4. Kullanıcı Arayüzü (UI) ve Kullanıcı Deneyimi (UX) Ön Tasarımı**
* **4.1. Genel Arayüz Yaklaşımı:**
    * `Uygulama genel olarak modern, minimalist ve kullanıcı dostu bir tasarıma sahip olacak. Wordle oyununun bilinen renk paletine (yeşil, sarı, gri) sadık kalınacak, bununla birlikte uygulamanın ana teması için sakin ve göz yormayan bir ana renk (örneğin, koyu mavi veya modern bir gri tonu) kullanılabilir. Odak noktası, oyun deneyiminin akıcı ve anlaşılır olmasıdır.`
* **4.2. Ana Ekranlar/Pencereler:**
    * `[Uygulamanızda olması muhtemel ana ekranları veya pencereleri listeleyin. Her birinin temel işlevi ne olacak? Örneğin: Ana Pencere, Ayarlar Penceresi, Veri Giriş Formu vb.]`
    * `[Eğer varsa, basit çizimler veya wireframe fikirlerinizi buraya not alabilirsiniz.]`
* **4.3. Kullanıcı Etkileşimleri:**
    * `[Kullanıcı uygulamayla nasıl etkileşim kuracak? Düğmeler, menüler, sürükle-bırak vb.?]`

---

**5. Teknik Detaylar**
* **5.1. Programlama Dili ve Ana Kütüphaneler/Frameworkler:**
    * **Dil:** Python (`[Python versiyonu, örn: 3.10+]`)
    * **Masaüstü Uygulama Çerçevesi:** `[Örn: Tkinter, PyQt5/6, Kivy, Flet, CustomTkinter vb. Neden bu seçimi yaptığınızı kısaca belirtin.]`
    * **Kullanılacak Diğer Önemli Python Kütüphaneleri:** `[Örn: pandas (veri işleme), matplotlib (grafik), requests (API), Pillow (görsel işleme) vb.]`
* **5.2. Veritabanı:**
    * **Veritabanı Sistemi:** MySQL
    * **Bağlantı Kütüphanesi:** `[Örn: mysql.connector, PyMySQL vb.]`
    * **Temel Veritabanı Şeması Fikirleri:**
        * **Tablo 1: `[Tablo Adı (örn: Kullanicilar)]`**
            * `[Sütun Adı 1 (örn: id)]`: `[Veri Tipi (örn: INT, PRIMARY KEY, AUTO_INCREMENT)]`
            * `[Sütun Adı 2 (örn: kullanici_adi)]`: `[Veri Tipi (örn: VARCHAR(255), UNIQUE)]`
            * `[Sütun Adı 3 (örn: sifre_hash)]`: `[Veri Tipi (örn: VARCHAR(255))]`
            * `...`
        * **Tablo 2: `[Tablo Adı]`**
            * `[Sütunlar ve Veri Tipleri]`
            * `...`
        * `[Tablolar arası ilişkileri (foreign keys) burada belirtebilirsiniz.]`
* **5.3. Geliştirme Araçları ve Ortamı:**
    * **IDE/Kod Editörü:** `[Örn: VS Code, PyCharm, Sublime Text]`
    * **Versiyon Kontrol Sistemi:** Git / GitHub
    * **Proje Yönetimi Aracı:** GitHub Projects
    * **Sanal Ortam Yönetimi:** `[Örn: venv, conda]`
    * **İşletim Sistemi:** `[Geliştirme yapacağınız işletim sistemi]`

---

**6. Proje Yapısı ve Mimarisi (Ön Fikirler)**
* **6.1. Klasör Yapısı:**
    * `[Proje dosyalarınızı nasıl bir klasör yapısında organize etmeyi düşünüyorsunuz? Örneğin: /src, /data, /tests, /docs, /ui_files vb.]`
* **6.2. Mimari Yaklaşım (İsteğe Bağlı):**
    * `[Eğer düşünüyorsanız, MVC, MVVM gibi bir mimari desen kullanacak mısınız? Ya da daha basit bir modüler yapı mı hedefliyorsunuz?]`

---

**7. Geliştirme Aşamaları / İterasyonlar (GitHub Projenizdeki Sütunlar/Sprintler İçin)**
* `[Projeyi hangi mantıksal aşamalara veya iterasyonlara bölmeyi planlıyorsunuz? Her aşamanın sonunda ne gibi bir çıktı/demo hedefleniyor?]`
    * **Aşama 1: Temel Kurulum ve Ana Arayüz**
        * `[Hedefler: Proje iskeletinin oluşturulması, veritabanı bağlantısının sağlanması, ana pencerenin tasarlanması.]`
        * `[Bu aşamaya dahil olacak özellikler/görevler (Bkz. Madde 3)]`
    * **Aşama 2: `[Aşama Adı (örn: Kullanıcı Yönetimi Özellikleri)]`**
        * `[Hedefler]`
        * `[Bu aşamaya dahil olacak özellikler/görevler]`
    * **Aşama 3: `[Aşama Adı (örn: Temel Veri İşleme Fonksiyonları)]`**
        * `[Hedefler]`
        * `[Bu aşamaya dahil olacak özellikler/görevler]`
    * `... (Gerektiği kadar aşama ekleyin)`

---

**8. Potansiyel Zorluklar ve Riskler**
* `[Proje geliştirme sürecinde karşılaşabileceğinizi düşündüğünüz olası zorluklar, riskler ve bunlara karşı alabileceğiniz önlemler veya çözüm stratejileriniz nelerdir?]`
    * `Örnek: Belirli bir Python kütüphanesini öğrenmek zaman alabilir -> Çözüm: Kütüphane için ayrı bir öğrenme/deneme süresi planlamak.`
    * `Örnek: Kullanıcı arayüzü tasarımında zorlanmak -> Çözüm: Benzer uygulamalardan ilham almak, basit wireframe'ler ile başlamak.`

---

**9. Öğrenme Hedefleri (Kişisel Gelişim)**
* `[Bu proje özelinde Python veya genel yazılım geliştirme ile ilgili olarak özellikle öğrenmeyi veya pekiştirmeyi hedeflediğiniz konular nelerdir?]`
    * `Örnek: Asenkron programlama, belirli bir tasarım deseni (design pattern) uygulamak, etkili birim testleri yazmak, CI/CD temelleri vb.`

---

**10. Gelecek Geliştirmeler (Projenin İlk Versiyonu Sonrası İçin Fikirler)**
* `[Projenin ilk versiyonu tamamlandıktan sonra eklemeyi düşünebileceğiniz veya hayal ettiğiniz ek özellikler, iyileştirmeler neler olabilir?]`
