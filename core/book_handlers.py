import book_transactions as bt
from core.menu import menu_header, print_details
import book_transactions as bt
from core.utils import show_message

def handle_show_books():
    menu_header("📚 Kütüphanedeki Kitaplar")
    books = bt.get_all_books()
    print_details(books)
    input("\nDevam etmek için bir tuşa basın...")

def handle_add_book():
    menu_header("📚 Yeni Kitap Ekle")

    barcode = input("Barkod: ").strip()
    title = input("Kitap Adı: ").strip()
    publisher = input("Yayınevi: ").strip()
    author = input("Yazar: ").strip()
    status = "available"

    # book_transactions içindeki fonksiyonu çağır
    bt.add_book(barcode, title, publisher, author, status)
    show_message(f"\n✅ '{title}' başarıyla eklendi.\n")

def handle_search_book():
    menu_header("🔍 Kitap Ara")
    search_term = input("Aramak istediğiniz kitap/başlık/yazar: ").strip()
    results = bt.search_book(search_term)
    
    if results:
        print("\n🔎 Arama Sonuçları:")
        print_details(results)
    else:
        print("❌ Aradığınız kriterlere uygun kitap bulunamadı.")
    input("\nDevam etmek için bir tuşa basın...")

def handle_delete_book():
    menu_header("🗑️ Kitap Sil")
    barcode = input("Silmek istediğiniz kitabın barkodu: ").strip()
    bt.delete_book(barcode)
    show_message("✅ Kitap başarıyla silindi.")