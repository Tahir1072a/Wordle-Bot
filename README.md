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
        * `Alt Görev/Detay: Kullanıcı uygulamaya başarılı bir şekilde giriş yaptığında, yönlendirileceği uygulama anasayfası tasarlanacaktır. Anasayfada Oyna, Bot Oynasın ve Çıkış butonları olacaktır.`
        * `Alt Görev/Detay: Kullanıcı bu anasayfa üzerinden oturumunu sonlandırabilecektir.`
        * `Alt Görev/Detay: Kullanıcı oyna butonu içerisinden direkt uygulamaya yönlendirme yapılacaktır. `
        * `Alt Görev/Detay: Bot oynasın butonu seçilirse, kontrol bota geçecek ve oyunu oynamaya başlayacak. `

* **B. Wordle Oyun Motorunu Geliştirmek**
    * **Özellik 4:** Wordle arayüzünün oluşturulması
        * `Alt görev/detay: 5 sutün, 6 satırdan oluşan bir grid (ızgara) oluşturulacak. Kullacını grid içerisine klavye üzerinden kelime girebilecek. Enter tuşuna bastığında ise kelime kontrol için ilgili işleve gönderilecek.`
        * `Alt görev/detay: Botun önerdiği ilk 10 kelime ve kelimelerin içerdiği bilgi teorisine dayalı skorları kullanıcıya grid'in yanında gösterilecektir. Her yeni kelime tahmininde burası güncellenecek şekilde dinamik olması gerekiyor.`
        * `Alt görev/detay: Girilen kelime, oyun için izin verilen kelimeler arasında var mı diye kontrol edilecek. Ona göre hata/başarı mesajı gönderilecek`
        * `Alt görev/detay: 6 denemede kullanıcı kelimeye ulaşamazsa, ekrana başarısız mesajı basılacak ve doğru kelime gösterilecek. Kullanıcı anasayfaya geri yönlendirilecek.`
    * **Özellik 5:** Wordle oyunun mantığının oluşturulması
        * `Alt görev/detay: Aranan kelimeye göre, harflerin konumuyla ilgili kullanıcıya geri bildirim yapılacak. (Konumu doğru ise: yeşil, konumu yanlış ise: sarı, hiçbir konumda yoksa: gri) rengini alacak şekilde grid kutucukları güncellenecek.`
        * `Alt görev/detay: Her oyun sonu kullanıcıya ait istatistikler (kaç tahminde buldu, kazandı/kaybetti vb.) veritabanına kaydedilecek.`
        * `Alt görev/detay: Oyna butonuna basıldığında, kelime havuzun rastgele bir kelime aranana kelime olarak seçilecek.`

* **C. Wordle Bot Geliştirmek**
  * **Özellik 6:** Wordle Bot Algortiması
    * `Alt görev/detay: Kelimelerin içerdiği bilgi miktarını hesaplayan bir mekanizma geliştirilecek. En yüksek bilgi miktarına sahip 10 kelimeyi ve bilgi miktarını bize vermesi gerekiyor.`
    * `Alt görev/detay: Bot, kelime yazıldıktan sonra harflerin rengine göre, elindeki kelime havuzunu filtreleyebilmesi gerekiyor.`
    * `Alt görev/detay: Botun kendi kendine arayüz ile etkileşime girip oynayabilmesini istiyorum. Oyuncu bot oynasın modunu seçtikten sonra, bot kelimeleri ekrana girebileceği, bir mekanizma geliştirilmesi lazım. Kullanıcı bu işlemi durdurana kadar tekrar eden sonsuz bir döngü.`
   
* **D. Diğer işlevler**
  * **Özellik 7:** Kullanıcı İstatistikleri
    * `Alt görev/detay: Kullanıcı oyun istatistiklerini görebileceği bir GUI ekranı tasarlanacak`
    * `Alt görev/detay: Kullanıcı anasayfadan oyun istatistiklerine ulaşabilecek. Oyun ile ilgili pasta grafiği vb. grafikler ile kullanıcıya güzel bir sunum yapılacak.`
  * **Özellik 8:** Helper Modülü
    * `Alt görev/detay: İnternet üzerinden kelime havuzu çekip, veritabanına kaydetme işlemleri helper modülü tarafından gerçekleştirilecek. Bu modül oyun kurulumu için gerekli konfigürasyonları içeren bir bileşen olarak kodlanması gerekiyor.`

---

**4. Kullanıcı Arayüzü (UI) ve Kullanıcı Deneyimi (UX) Ön Tasarımı**
* **4.1. Genel Arayüz Yaklaşımı:**
    * `Uygulama genel olarak modern, minimalist ve kullanıcı dostu bir tasarıma sahip olacak. Wordle oyununun bilinen renk paletine (yeşil, sarı, gri) sadık kalınacak, bununla birlikte uygulamanın ana teması için sakin ve göz yormayan bir ana renk (örneğin, koyu mavi veya modern bir gri tonu) kullanılabilir. Odak noktası, oyun deneyiminin akıcı ve anlaşılır olmasıdır.`
* **4.2. Ana Ekranlar/Pencereler:**
    * `Giriş Ekranı: Oyuna giriş yapmak, kayıt olmak için kullanılacak pencere bu olacaktır.`
    * `Ana Ekran: Oyuna giriş yapıldıktan sonra kullanıcının yönlendirileceği bir pencere olacaktır. Buradan kullanıcı oyun istatistiklerini görüntüleyebilecek, oyuna başlayabilecek, çıkış yapabilecek veyahut bot oynasın seçeneğine tıklayabilecektir.`
    * `Oyun Ekranı: Burada grid yapısı ile kulalnıcın harfleri girebileceği oyun ekranı karşımıza gelecektir. Ayrıca kullanıcı bu ekranda botun önerdiği kelime listesini de görebilecek.`
    * `İstatistik Ekranı: Kullanıcın genel bilgilerini ve oynadığı oyun istatistiklerini görüntüleyebildiği ekran olacaktır.`

---

**5. Teknik Detaylar**
* **5.1. Programlama Dili ve Ana Kütüphaneler/Frameworkler:**
    * **Dil:** Python (3.9+)
    * **Masaüstü Uygulama Çerçevesi:** PyQT5
         * *Seçim Gerekçesi*: PyQt5, hem güçlü bir GUI çerçevesi sunması, hem de profesyonel uygulamalar için endüstri standardı olması nedeniyle seçilmiştir. Geniş dokümantasyonu ve topluluğu bulunması, geliştiriciye zengin kaynak sağlar.
    * **Kullanılacak Diğer Önemli Python Kütüphaneleri:** NumPy/Pandas: İstatistik ve veri yönetimi için ve smtplib: Mail gönderme işlemleri için
* **5.2. Veritabanı:**
    * **Veritabanı Sistemi:** MySQL
    * **Bağlantı Kütüphanesi:** mysql.connector
    * **Temel Veritabanı Şeması Fikirleri:**
        * **Tablo 1: Users**
            * Id
            * Username
            * Email
            * Password
        * **Tablo 2: Statistics**
            * Id
            * UserId (foreign key)
            * Total Game Number
            * Game Won Number
            * Game Lose Number
            * Avarage Score
        * **Tablo 3: Words**
            * Id
            * Word
        * **Tablo 4: Game**
            * Id
            * UserId (foreign key)
            * WordId (foreign key)
            * Score
            * Win or Lose
* **5.3. Geliştirme Araçları ve Ortamı:**
    * **IDE/Kod Editörü:** PyCharm
    * **Versiyon Kontrol Sistemi:** Git / GitHub
    * **Proje Yönetimi Aracı:** GitHub Projects
    * **Sanal Ortam Yönetimi:** Conda
    * **İşletim Sistemi:** Windows

---

**6. Proje Yapısı ve Mimarisi **
* **6.1. Klasör Yapısı:**
   * wordle_bot/

│

├── src/                        # Kaynak kod ana dizini

│   ├── main.py                 # Uygulama giriş noktası

│   ├── config.py               # Yapılandırma dosyası

│   │

│   ├── model/                  # Veri modeli sınıfları

│   │   ├── user.py             # Kullanıcı modeli

│   │   ├── game.py             # Oyun modeli

│   │   ├── word.py             # Kelime modeli

│   │   └── statistics.py       # İstatistik modeli

│   │

│   ├── view/                   # GUI dosyaları

│   │   ├── login.py            # Giriş ekranı

│   │   ├── registration.py     # Kayıt ekranı

│   │   ├── main_window.py      # Ana menü

│   │   ├── game_board.py       # Oyun tahtası

│   │   ├── stats_view.py       # İstatistik ekranı

│   │   └── settings.py         # Ayarlar ekranı

│   │

│   ├── controller/             # Kontrol mantığı

│   │   ├── auth_controller.py  # Kimlik doğrulama kontrolcüsü

│   │   ├── game_controller.py  # Oyun kontrolcüsü

│   │   ├── bot_controller.py   # Bot kontrolcüsü

│   │   └── stat_controller.py  # İstatistik kontrolcüsü

│   │

│   ├── db/                     # Veritabanı işlemleri

│   │   ├── db_connector.py     # Veritabanı bağlantısı

│   │   ├── user_repo.py        # Kullanıcı veritabanı işlemleri

│   │   ├── word_repo.py        # Kelime veritabanı işlemleri

│   │   └── game_repo.py        # Oyun veritabanı işlemleri

│   │

│   ├── bot/                    # Bot algoritmaları

│   │   ├── entropy.py          # Entropy hesaplama

│   │   ├── word_filter.py      # Kelime filtreleme

│   │   └── suggestion.py       # Öneri algoritması

│   │

│   └── utils/                  # Yardımcı fonksiyonlar

│       ├── validators.py       # Doğrulama fonksiyonları

│       ├── email_service.py    # E-posta gönderme servisi

│       ├── word_fetcher.py     # Kelime listesi getirme

│       └── logger.py           # Loglama yardımcısı

│

├── tests/                      # Test dosyaları

│   ├── test_game_logic.py

│   ├── test_bot.py

│   └── test_db.py

│

├── resources/                  # Kaynak dosyaları

│   ├── styles/                 # CSS stilleri

│   ├── images/                 # Görsel dosyalar

│   ├── wordlists/              # Kelime listeleri

│   └── ui/                     # Qt Designer UI dosyaları

│

├── docs/                       # Belgelendirme

│   ├── api/                    # API belgelendirmesi

│   └── user_guide/             # Kullanıcı kılavuzu

│

├── scripts/                    # Yardımcı scriptler

│   ├── setup_db.py             # Veritabanı kurulum scripti

│   └── word_importer.py        # Kelime içe aktarma scripti

│

├── .gitignore

├── README.md

├── requirements.txt            # Bağımlılıklar

└── setup.py                    # Kurulum dosyası

* **6.2. Mimari Yaklaşım:**
    * MVC yaklaşımı benimsenecektir.

---

**10. Gelecek Geliştirmeler (Projenin İlk Versiyonu Sonrası İçin Fikirler)**
* İlerleyen aşamalarda oyunweb üzerinden online bir şekilde oynanabilmesi için geliştirilebilir.
