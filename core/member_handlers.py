import member_transactions as mt
from core.menu import menu_header, print_details
from core.utils import show_message
import member_transactions as mt
from tracking import track_loan


def handle_show_members():
    menu_header("👥 Kayıtlı Üyeler")
    members = mt.get_all_members()
    print_details(members)
    input("\nDevam etmek için bir tuşa basın...")


def handle_add_member():
    menu_header("🆕 Yeni Üyelik")
    name = input("Ad Soyad: ").strip()
    phone = input("Telefon Numarası: ").strip()
    address = input("Adres: ").strip()

    mt.add_member(name, phone, address)
    show_message("\n✅ Üyelik başarıyla oluşturuldu.")


def handle_search_member():
    menu_header("🔍 Üye Arama")
    keyword = input("Aranacak isim veya ID: ").strip()
    results = mt.search_member(keyword)
    
    if results:
        print("\n🔎 Eşleşen Üyeler:")
        print_details(results)
    else:
        print("❌ Üye bulunamadı.")
    input("\nDevam etmek için bir tuşa basın...")


def handle_delete_member():
    menu_header("🗑️ Üyelik Sil")
    member_id = input("Silinecek Üyenin ID'si: ").strip()
    mt.delete_member(member_id)
    show_message("\n✅ Üyelik başarıyla silindi.")


def handle_loan_book():
    menu_header("📕 Kitap Ödünç Ver")
    member_id = input("Üye ID: ").strip()
    barcode = input("Kitap Barkodu: ").strip()

    success = mt.lend_book(member_id, barcode)
    if success:
        print("\n✅ Kitap başarıyla ödünç verildi.")
    else:
        print("❌ Kitap şu anda ödünç verilemez.")
    input("\nDevam etmek için bir tuşa basın...")


def handle_return_book():
    menu_header("📗 Kitap İade")
    member_id = input("Üye ID: ").strip()
    barcode = input("İade edilecek Kitap Barkodu: ").strip()

    success = mt.return_book(member_id, barcode)
    if success:
        print("\n✅ Kitap iadesi başarıyla yapıldı.")
    else:
        print("❌ İade işlemi başarısız.")
    input("\nDevam etmek için bir tuşa basın...")


def handle_book_tracking():
    menu_header("📊 Kitap Takibi")
    member_id = input("Üye ID: ").strip()
    loans = track_loan(member_id)

    if loans:
        print("\n📚 Ödünç Alınan Kitaplar:")
        print_details(loans)
    else:
        print("ℹ️ Bu üyenin aktif ödünç aldığı kitap bulunmamaktadır.")
    input("\nDevam etmek için bir tuşa basın...")
