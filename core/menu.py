from core.utils import *

def menu_header(menu_name, menu_width=30):
    clear_screen()
    print('-' * menu_width)
    print('|' + f"\033[1;33m"+ menu_name.center(menu_width - 2)+f"\033[0m" + '|')
    print('-' * menu_width)

def display_menu(title, options, width=50):
    menu_header(title, width)
    for option in options:
        print('|' + ' ' * 10 + option.ljust(width - 12) + '|')
    print('-' * width)

def display_main_menu():
    main_menu = [
        "1 - ÜYELİK İŞLEMLERİ",
        "2 - KİTAP İŞLEMLERİ",
        "0 - ÇIKIŞ"
    ]

    display_menu("HALK KÜTÜPHANEMİZE HOŞGELDİNİZ", main_menu)

def display_members_menu():    
    member_menu = [
        "1 - ÜYELERİ GÖSTER",
        "2 - ÜYELİK EKLE",
        "3 - ÜYE ARA",
        "4 - ÜYELİK SİL",
        "5 - KİTAP ÖDÜNÇ VER",
        "6 - KİTAP İADE",
        "7 - KİTAP TAKİBİ",
        "0 - ÇIKIŞ"
    ]

    display_menu("ÜYELİK İŞLEMLERİ", member_menu)

def display_books_menu():    
    book_menu = [
        "1 - KİTAPLARI GÖSTER",
        "2 - KİTAP EKLE",
        "3 - KİTAP ARA",
        "4 - KİTAP SİL",
        "0 - ÇIKIŞ"
    ]
    display_menu("KİTAP İŞLEMLERİ (ENVANTER)", book_menu)        
