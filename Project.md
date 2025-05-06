**Veri Dosyaları:**

* **`book.json`**: Kitapları (ID, başlık, yazar, yayın yılı, durum vb.) liste halinde saklar.
* **`member.json`**: Üyeleri (ID, isim, vb.) liste halinde saklar.
* **`tracking.json`**: Hangi üyenin hangi kitabı ne zaman aldığını ve ne zaman iade etmesi gerektiğini takip eden kayıtları liste halinde saklar.

---

## Görev Dağılımı

### Kürşad (Takım Lideri)

* **Sorumlu Olduğu Modüller:** `main.py`, `time_utils.py`
* **Genel Görevler:** Projenin genel akışını yönetmek, modüller arası entegrasyonu sağlamak, kullanıcı arayüzünü oluşturmak, zaman hesaplamalarını yapmak.

* **`main.py` Görevleri:**
    * Kullanıcıya ana menüyü sunmak (Kitap Ekle/Sil/Ara, Üye Ekle/Sil/Ara, Kitap Ödünç Ver/Al vb.).
    * Kullanıcıdan girdi almak ve ilgili modüldeki fonksiyonları çağırmak.
    * Gerekli modülleri (`book_transactions`, `member_transactions`, `time_utils`) import etmek.
    * Uygulama başlangıcında gerekli JSON dosyalarının varlığını kontrol etmek (os modülü ile), yoksa boş listelerle oluşturmak.
    * Fonksiyon çağrılarından dönen sonuçları kullanıcıya göstermek.
    * Hata yönetimini (örn. geçersiz kullanıcı girdisi) temel düzeyde yönetmek.

* **`time_utils.py` Görevleri:**
    * **Gerekli İmportlar:** `datetime`
    * **Fonksiyonlar:**
        * `get_current_timestamp()`:
            * **Açıklama:** Mevcut anın tarih ve saat bilgisini döndürür.
            * **Parametreler:** Yok.
            * **Döndürdüğü Değer:** `datetime` objesi veya formatlanmış string (örn. 'YYYY-MM-DDTHH:MM:SS').
            * ```python
              import datetime

              def get_current_timestamp():
                  """Returns the current date and time."""
                  # Örnek: return datetime.datetime.now()
                  pass
              ```
        * `calculate_due_date(start_date, weeks=2)`:
            * **Açıklama:** Verilen başlangıç tarihinden itibaren belirli bir hafta sonrası tarihi hesaplar.
            * **Parametreler:** `start_date` (datetime objesi veya uyumlu string), `weeks` (int, varsayılan 2).
            * **Döndürdüğü Değer:** `datetime` objesi veya formatlanmış string (örn. 'YYYY-MM-DDTHH:MM:SS').
            * ```python
              import datetime

              def calculate_due_date(start_date, weeks=2):
                  """Calculates the date two weeks after the start_date."""
                  # Örnek: return start_date + datetime.timedelta(weeks=weeks)
                  pass
              ```

---

### Furkan

* **Sorumlu Olduğu Modül:** `book_transactions.py` (Kısmen)
* **Genel Görevler:** Kitap ekleme, silme, arama ve JSON dosyasını okuma/yazma işlemlerinin temelini oluşturmak. Mehmet Lütfi ile koordineli çalışacak.

* **`book_transactions.py` Görevleri:**
    * **Gerekli İmportlar:** `json`, `os`
    * **Fonksiyonlar:**
        * `_load_books(filepath='book.json')`:
            * **Açıklama:** Kitap verilerini JSON dosyasından yükler. Dosya yoksa veya boşsa boş liste döndürür. (Bu fonksiyon modül içinde private olabilir `_` ile)
            * **Parametreler:** `filepath` (string, dosya yolu).
            * **Döndürdüğü Değer:** Kitap listesi (`list`).
            * ```python
              import json
              import os

              def _load_books(filepath='book.json'):
                  """Loads books from the JSON file."""
                  if not os.path.exists(filepath):
                      return []
                  try:
                      with open(filepath, 'r', encoding='utf-8') as f:
                          data = json.load(f)
                          return data
                  except (json.JSONDecodeError, FileNotFoundError):
                      return [] # Return empty list on error or empty file
                  pass # Placeholder - Implement file reading
              ```
        * `_save_books(books, filepath='book.json')`:
            * **Açıklama:** Güncel kitap listesini JSON dosyasına kaydeder. (Bu fonksiyon modül içinde private olabilir `_` ile)
            * **Parametreler:** `books` (list, kaydedilecek kitap listesi), `filepath` (string, dosya yolu).
            * **Döndürdüğü Değer:** Yok (`None`).
            * ```python
              import json

              def _save_books(books, filepath='book.json'):
                  """Saves the books list to the JSON file."""
                  try:
                      with open(filepath, 'w', encoding='utf-8') as f:
                          json.dump(books, f, indent=4, ensure_ascii=False)
                  except IOError:
                      print(f"Error: Could not write to file {filepath}")
                  pass # Placeholder - Implement file writing
              ```
        * `add_book(title, author, publication_year, book_id)`:
            * **Açıklama:** Yeni bir kitabı listeye ekler ve dosyayı günceller. ID'nin benzersizliğini kontrol edebilir.
            * **Parametreler:** `title` (str), `author` (str), `publication_year` (int), `book_id` (str, örn. ISBN).
            * **Döndürdüğü Değer:** Başarılı ise `True`, kitap zaten varsa veya hata oluşursa `False`.
            * ```python
              def add_book(title, author, publication_year, book_id):
                  """Adds a new book to the library."""
                  # books = _load_books()
                  # Check if book_id already exists
                  # If not, create new book dict {'book_id': ..., 'status': 'available', ...}
                  # append to books list
                  # _save_books(books)
                  pass
              ```
        * `delete_book(book_id)`:
            * **Açıklama:** Verilen ID'ye sahip kitabı listeden siler ve dosyayı günceller. Kitabın ödünçte olup olmadığını kontrol etmek gerekebilir (Ali'nin fonksiyonlarıyla entegrasyon).
            * **Parametreler:** `book_id` (str).
            * **Döndürdüğü Değer:** Başarılı ise `True`, kitap bulunamazsa veya silinemezse `False`.
            * ```python
              def delete_book(book_id):
                  """Deletes a book from the library by its ID."""
                  # books = _load_books()
                  # Find book by book_id
                  # Ensure book is 'available' before deleting (or handle borrowed case)
                  # Remove from list
                  # _save_books(books)
                  pass
              ```
        * `search_book(query, search_by='title')`:
            * **Açıklama:** Başlık, yazar veya ID'ye göre kitap arar.
            * **Parametreler:** `query` (str, aranan değer), `search_by` (str, 'title', 'author', veya 'book_id').
            * **Döndürdüğü Değer:** Eşleşen kitapların listesi (`list`). Eşleşme yoksa boş liste.
            * ```python
              def search_book(query, search_by='title'):
                  """Searches for books by title, author, or ID."""
                  # books = _load_books()
                  # Filter books based on query and search_by field
                  # Return list of matching books
                  pass
              ```

---

### Mehmet Lütfi

* **Sorumlu Olduğu Modül:** `book_transactions.py` (Kısmen)
* **Genel Görevler:** Kitap güncelleme, listeleme ve varlık kontrolü fonksiyonlarını yazmak. Furkan ile koordineli çalışacak.

* **`book_transactions.py` Görevleri:**
    * **Gerekli İmportlar:** `json`, `os` (Furkan'ın yazdığı `_load_books` ve `_save_books` fonksiyonlarını kullanacak)
    * **Fonksiyonlar:**
        * `update_book(book_id, new_data)`:
            * **Açıklama:** Verilen ID'ye sahip kitabın bilgilerini günceller.
            * **Parametreler:** `book_id` (str), `new_data` (dict, güncellenecek alanları içerir, örn. `{'title': 'Yeni Başlık', 'status': 'borrowed'}`).
            * **Döndürdüğü Değer:** Başarılı ise `True`, kitap bulunamazsa `False`.
            * ```python
              # Requires _load_books and _save_books from Furkan
              def update_book(book_id, new_data):
                  """Updates information for a specific book."""
                  # books = _load_books()
                  # Find the book by book_id
                  # Update the book's dictionary with new_data
                  # _save_books(books)
                  pass
              ```
        * `list_all_books()`:
            * **Açıklama:** Kütüphanedeki tüm kitapları listeler.
            * **Parametreler:** Yok.
            * **Döndürdüğü Değer:** Tüm kitapların listesi (`list`).
            * ```python
              # Requires _load_books from Furkan
              def list_all_books():
                  """Returns a list of all books in the library."""
                  # return _load_books()
                  pass
              ```
        * `check_book_availability(book_id)`:
            * **Açıklama:** Verilen ID'ye sahip kitabın ödünç alınıp alınamayacağını kontrol eder ('available' durumunda mı?).
            * **Parametreler:** `book_id` (str).
            * **Döndürdüğü Değer:** Kitap mevcut ve 'available' ise `True`, değilse `False`.
            * ```python
              # Requires _load_books from Furkan
              def check_book_availability(book_id):
                  """Checks if a book exists and is available for borrowing."""
                  # books = _load_books()
                  # Find book by book_id
                  # Return True if book exists and book['status'] == 'available', else False
                  pass
              ```
        * `get_book_details(book_id)`:
             * **Açıklama:** Verilen ID'ye sahip kitabın tüm detaylarını getirir.
             * **Parametreler:** `book_id` (str).
             * **Döndürdüğü Değer:** Kitap bulunduysa kitap sözlüğü (`dict`), bulunamadıysa `None`.
             * ```python
               # Requires _load_books from Furkan
               def get_book_details(book_id):
                   """Gets the details of a specific book by its ID."""
                   # books = _load_books()
                   # Find book by book_id
                   # Return the book dictionary if found, else return None
                   pass
               ```


---

### Mustafa

* **Sorumlu Olduğu Modül:** `member_transactions.py` (Kısmen)
* **Genel Görevler:** Üye ekleme, silme, arama, güncelleme, listeleme ve üye JSON dosyasını okuma/yazma işlemlerini yapmak. Ali ile koordineli çalışacak.

* **`member_transactions.py` Görevleri:**
    * **Gerekli İmportlar:** `json`, `os`, `datetime` (veya Kürşad'ın `time_utils` modülü)
    * **Fonksiyonlar:**
        * `_load_members(filepath='member.json')`:
            * **Açıklama:** Üye verilerini JSON dosyasından yükler. Dosya yoksa veya boşsa boş liste döndürür. (Private olabilir)
            * **Parametreler:** `filepath` (string).
            * **Döndürdüğü Değer:** Üye listesi (`list`).
            * ```python
              import json
              import os

              def _load_members(filepath='member.json'):
                  """Loads members from the JSON file."""
                  if not os.path.exists(filepath):
                      return []
                  try:
                      with open(filepath, 'r', encoding='utf-8') as f:
                          data = json.load(f)
                          return data
                  except (json.JSONDecodeError, FileNotFoundError):
                      return []
                  pass # Implement
              ```
        * `_save_members(members, filepath='member.json')`:
            * **Açıklama:** Güncel üye listesini JSON dosyasına kaydeder. (Private olabilir)
            * **Parametreler:** `members` (list), `filepath` (string).
            * **Döndürdüğü Değer:** Yok (`None`).
            * ```python
              import json

              def _save_members(members, filepath='member.json'):
                  """Saves the members list to the JSON file."""
                  try:
                      with open(filepath, 'w', encoding='utf-8') as f:
                          json.dump(members, f, indent=4, ensure_ascii=False)
                  except IOError:
                      print(f"Error: Could not write to file {filepath}")
                  pass # Implement
              ```
        * `add_member(name, member_id)`:
            * **Açıklama:** Yeni üye ekler. ID'nin benzersizliğini kontrol etmeli. Katılım tarihini otomatik eklemeli.
            * **Parametreler:** `name` (str), `member_id` (str, örn. 'M003').
            * **Döndürdüğü Değer:** Başarılı ise `True`, üye zaten varsa veya hata oluşursa `False`.
            * ```python
              # May need: import datetime or from time_utils import get_current_timestamp
              def add_member(name, member_id):
                  """Adds a new member."""
                  # members = _load_members()
                  # Check if member_id exists
                  # Get current date for join_date
                  # Create member dict {'member_id': ..., 'name': ..., 'join_date': ..., 'borrowed_books_count': 0}
                  # append to members list
                  # _save_members(members)
                  pass
              ```
        * `delete_member(member_id)`:
            * **Açıklama:** Verilen ID'ye sahip üyeyi siler. Üyenin ödünç kitabı olup olmadığını kontrol etmek gerekebilir (Ali'nin fonksiyonlarıyla entegrasyon).
            * **Parametreler:** `member_id` (str).
            * **Döndürdüğü Değer:** Başarılı ise `True`, üye bulunamazsa veya kitabı varsa `False`.
            * ```python
              def delete_member(member_id):
                  """Deletes a member by ID."""
                  # members = _load_members()
                  # Check if member has borrowed books (needs integration with tracking data)
                  # Find member by member_id
                  # Remove from list
                  # _save_members(members)
                  pass
              ```
        * `search_member(query, search_by='name')`:
            * **Açıklama:** İsim veya ID'ye göre üye arar.
            * **Parametreler:** `query` (str), `search_by` (str, 'name' veya 'member_id').
            * **Döndürdüğü Değer:** Eşleşen üyelerin listesi (`list`).
            * ```python
              def search_member(query, search_by='name'):
                  """Searches for members by name or ID."""
                  # members = _load_members()
                  # Filter members based on query and search_by
                  # Return list of matching members
                  pass
              ```
        * `update_member(member_id, new_data)`:
             * **Açıklama:** Verilen ID'ye sahip üyenin bilgilerini günceller (örn. isim değişikliği). `borrowed_books_count` alanı Ali tarafından güncellenecek.
             * **Parametreler:** `member_id` (str), `new_data` (dict, örn. `{'name': 'Yeni İsim'}`).
             * **Döndürdüğü Değer:** Başarılı ise `True`, üye bulunamazsa `False`.
             * ```python
               def update_member(member_id, new_data):
                   """Updates member information (e.g., name)."""
                   # members = _load_members()
                   # Find member by member_id
                   # Update member's dictionary (excluding borrowed_books_count maybe)
                   # _save_members(members)
                   pass
               ```
        * `list_all_members()`:
            * **Açıklama:** Tüm üyeleri listeler.
            * **Parametreler:** Yok.
            * **Döndürdüğü Değer:** Tüm üyelerin listesi (`list`).
            * ```python
              def list_all_members():
                  """Returns a list of all members."""
                  # return _load_members()
                  pass
              ```
        * `check_member_exists(member_id)`:
             * **Açıklama:** Verilen ID'ye sahip bir üyenin olup olmadığını kontrol eder.
             * **Parametreler:** `member_id` (str).
             * **Döndürdüğü Değer:** Üye varsa `True`, yoksa `False`.
             * ```python
               def check_member_exists(member_id):
                   """Checks if a member exists by ID."""
                   # members = _load_members()
                   # Check if any member in the list has the given member_id
                   pass
               ```

---

### Ali

* **Sorumlu Olduğu Modül:** `member_transactions.py` (Kısmen)
* **Genel Görevler:** Kitap ödünç verme ve iade alma mekanizmalarını kurmak, `tracking.json` dosyasını yönetmek. Mustafa, Kürşad, Furkan ve Mehmet Lütfi ile koordineli çalışacak.

* **`member_transactions.py` Görevleri:**
    * **Gerekli İmportlar:** `json`, `os`, `uuid` (tracking_id için), `datetime` (veya `time_utils` modülü), `book_transactions` modülünden ilgili fonksiyonlar (örn. `update_book`, `check_book_availability`, `get_book_details`).
    * **Fonksiyonlar:**
        * `_load_tracking_data(filepath='tracking.json')`:
            * **Açıklama:** Ödünç alma takip verilerini JSON dosyasından yükler. (Private olabilir)
            * **Parametreler:** `filepath` (string).
            * **Döndürdüğü Değer:** Takip kayıtları listesi (`list`).
            * ```python
              import json
              import os

              def _load_tracking_data(filepath='tracking.json'):
                  """Loads borrowing tracking data from the JSON file."""
                  if not os.path.exists(filepath):
                      return []
                  try:
                      with open(filepath, 'r', encoding='utf-8') as f:
                          data = json.load(f)
                          return data
                  except (json.JSONDecodeError, FileNotFoundError):
                      return []
                  pass # Implement
              ```
        * `_save_tracking_data(tracking_data, filepath='tracking.json')`:
            * **Açıklama:** Güncel takip verilerini JSON dosyasına kaydeder. (Private olabilir)
            * **Parametreler:** `tracking_data` (list), `filepath` (string).
            * **Döndürdüğü Değer:** Yok (`None`).
            * ```python
              import json

              def _save_tracking_data(tracking_data, filepath='tracking.json'):
                  """Saves the tracking data list to the JSON file."""
                  try:
                      with open(filepath, 'w', encoding='utf-8') as f:
                          json.dump(tracking_data, f, indent=4, ensure_ascii=False)
                  except IOError:
                       print(f"Error: Could not write to file {filepath}")
                  pass # Implement
              ```
        * `lend_book_to_member(member_id, book_id)`:
            * **Açıklama:** Bir üyeye kitap ödünç verir. Üye ve kitabın varlığını/uygunluğunu kontrol eder. `tracking.json`'a kayıt ekler. `book.json`'daki kitabın durumunu günceller (veya kitabı siler - proje tanımına göre). Üyenin ödünç aldığı kitap sayısını artırır (`member.json`).
            * **Gerekenler:** `check_member_exists` (Mustafa), `check_book_availability` (Mehmet Lütfi), `update_book` (Mehmet Lütfi), `get_current_timestamp` (Kürşad), `calculate_due_date` (Kürşad), `update_member` (Mustafa - dolaylı olarak count güncellemesi için veya ayrı fonksiyon).
            * **Parametreler:** `member_id` (str), `book_id` (str).
            * **Döndürdüğü Değer:** Başarılı ise `True`, hata durumunda (üye yok, kitap yok/ödünçte) `False`.
            * ```python
              import uuid
              # import book_transactions
              # import time_utils (veya import datetime)
              # from member_transactions import check_member_exists, update_member (veya _load/_save)

              def lend_book_to_member(member_id, book_id):
                  """Lends a book to a member and updates records."""
                  # 1. Check if member exists (use check_member_exists)
                  # 2. Check if book exists and is available (use check_book_availability)
                  # 3. If both checks pass:
                  #    a. Get current time (use get_current_timestamp)
                  #    b. Calculate due date (use calculate_due_date)
                  #    c. Create a unique tracking_id (e.g., using uuid.uuid4())
                  #    d. Create tracking record dict
                  #    e. Load tracking data, append record, save tracking data
                  #    f. Update book status to 'borrowed' in book.json (use update_book) OR remove book from book.json (per project spec)
                  #    g. Update member's borrowed_books_count in member.json (load members, find member, update count, save members)
                  #    h. Return True
                  # 4. If checks fail, return False
                  pass
              ```
        * `return_book_from_member(tracking_id)`:
            * **Açıklama:** Üyenin iade ettiği kitabı sisteme geri alır. `tracking.json`'dan ilgili kaydı siler (veya durumunu 'returned' yapar). `book.json`'a kitabı geri ekler veya durumunu 'available' yapar. Üyenin ödünç aldığı kitap sayısını azaltır.
            * **Gerekenler:** `add_book` (Furkan) veya `update_book` (Mehmet Lütfi), `update_member` (Mustafa - dolaylı olarak count güncellemesi için).
            * **Parametreler:** `tracking_id` (str) - Ödünç verme sırasında oluşturulan benzersiz ID. Alternatif olarak `member_id` ve `book_id` de kullanılabilir ancak `tracking_id` daha nettir.
            * **Döndürdüğü Değer:** Başarılı ise `True`, kayıt bulunamazsa `False`.
            * ```python
              # import book_transactions
              # from member_transactions import update_member (veya _load/_save)

              def return_book_from_member(tracking_id):
                  """Processes a returned book."""
                  # 1. Load tracking data
                  # 2. Find the tracking record by tracking_id
                  # 3. If found:
                  #    a. Get member_id and book_id from the record
                  #    b. Remove the record from tracking data, save tracking data
                  #    c. Update book status to 'available' in book.json (use update_book) OR add book back to book.json if it was deleted (use add_book - might need book details)
                  #    d. Update member's borrowed_books_count in member.json (load members, find member, decrease count, save members)
                  #    e. Return True
                  # 4. If record not found, return False
                  pass
              ```
        * `list_borrowed_books(member_id=None)`:
             * **Açıklama:** Belirli bir üyenin veya tüm üyelerin ödünç aldığı kitapları (ve iade tarihlerini) listeler.
             * **Parametreler:** `member_id` (str, opsiyonel). Belirtilmezse tüm ödünçteki kitaplar listelenir.
             * **Döndürdüğü Değer:** İlgili takip kayıtlarının listesi (`list`).
             * ```python
               def list_borrowed_books(member_id=None):
                   """Lists all borrowed books, optionally filtered by member."""
                   # tracking_data = _load_tracking_data()
                   # if member_id:
                   #     Filter tracking_data for the given member_id
                   # Return the filtered (or full) list
                   pass
               ```

---

**Genel Notlar ve Talimatlar:**

1.  **JSON Kullanımı:** Tüm veriler (`books.json`, `members.json`, `tracking.json`) JSON formatında saklanacaktır. Veri okuma (`json.load`) ve yazma (`json.dump`) işlemleri için Python'ın `json` modülünü kullanın. Yazarken `indent=4` ve `ensure_ascii=False` parametrelerini kullanmak okunabilirliği artırır.
2.  **Dosya Kontrolü:** `os` modülünü kullanarak (`os.path.exists`), bir JSON dosyasını okumadan önce var olup olmadığını kontrol edin. Dosya yoksa veya boşsa, hata almak yerine boş bir liste (`[]`) ile başlayın.
3.  **Hata Yönetimi:** `try...except` bloklarını kullanarak olası hataları (örn. `FileNotFoundError`, `json.JSONDecodeError`, `IOError`) yakalayın ve kullanıcıya anlamlı mesajlar verin veya programın çökmesini engelleyin.
4.  **İngilizce Fonksiyon İsimleri:** Fonksiyon isimleri, parametreler ve değişkenler için anlaşılır İngilizce terimler kullanın (istendiği gibi).
5.  **Fonksiyon İmplementasyonu:** Herkes kendi fonksiyonlarının içini doldururken, sadece `pass` yerine fonksiyonun ne yapması gerektiğini açıklayan yorumlar ve temel mantık adımlarını ekleyebilir. Tam kodu yazmak bir sonraki aşamadır.
6.  **İşbirliği:** Özellikle `member_transactions.py` üzerinde çalışan Ali ve Mustafa'nın, ayrıca `book_transactions.py` üzerinde çalışan Furkan ve Mehmet Lütfi'nin sık sık iletişimde olması ve fonksiyonların birbirleriyle nasıl etkileşeceğini planlaması önemlidir. Örneğin, Ali'nin `lend_book_to_member` fonksiyonu, Mehmet Lütfi'nin `update_book` fonksiyonunu çağıracaktır.
7.  **Benzersiz ID'ler:** Kitaplar (`book_id`, örn. ISBN) ve Üyeler (`member_id`) için benzersiz ID'ler kullanın. Yeni eklemelerde bu ID'lerin zaten var olup olmadığını kontrol edin. `tracking.json` için `uuid` modülü ile (`uuid.uuid4()`) otomatik benzersiz ID üretebilirsiniz.
8.  **Kod Standardı:** Mümkün olduğunca PEP 8 Python kodlama standartlarına uymaya çalışın (girintileme, isimlendirme vb.).