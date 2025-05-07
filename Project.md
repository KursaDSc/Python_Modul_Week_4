✅ Kürşad (Takım Lideri)
Sorumlu Olduğun Dosyalar:

        main.py
        core/menu.py
        core/routing.py
        core/book_handlers.py
        core/member_handlers.py

🧭 Proje akışı, yönlendirme, handler mantığı ve kullanıcı arayüzünün (CLI) temelinden sorumlu.

👤 Furkan – Kitap İşlemleri
Dosyalar:

        book_transactions.py
        data/books.json

Görevler:

- Kitap ekleme, silme, güncelleme, arama, listeleme

- Kitap verileriyle ilgili book_transactions.py fonksiyonlarını yazmak

- JSON veri dosyasıyla etkileşim için data_io.py’ye veri çağrısı yapmak

👤 Mustafa – Üye (Member) İşlemleri
Dosyalar:

        member_transactions.py
        data/members.json

Görevler:

- Üye ekleme, silme, arama, listeleme

- Kitap ödünç verme / iade işlemlerini member_transactions.py içinde gerçekleştirmek

- Üye bilgilerini işlemek için data_io.py ile veri alışverişi yapmak

👤 Ali – Takip Sistemi ve Zaman İşlemleri
Dosyalar:

        tracking.py
        data/tracking.json
        core/time_utils.py

Görevler:

- Ödünç alınan kitapların izlenmesi (kim aldı, ne zaman, vs.)

- Geciken kitapların takibi ve listeleme

- Tarih ve zaman hesaplamaları (geç kaldı mı? kaç gün kaldı?)

- time_utils.py içinde gerekli tarih fonksiyonlarını yazmak

👤 Mehmet Lütfi – Ortak JSON Veri Yönetimi
Dosyalar:

        core/data_io.py

Görevler:

- Tüm JSON veri dosyalarıyla okuma/yazma işlemleri

- book_transactions, member_transactions, tracking gibi modüllerin ihtiyaç duyduğu genel veri erişim fonksiyonlarını yazmak

- Gerekirse yedekleme veya ilk veri oluşturma (örneğin kitap_backup.json)
