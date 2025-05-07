import book_transactions
import os
import json
import core.time_utils as tu

def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
    
def save_members(members):
    with open("members.json", 'w', encoding='utf-8') as f:
        json.dump(members, f, indent=4, ensure_ascii=False)      

<<<<<<< Updated upstream
def add_member(name, phone, address):
    name = input("Üye adı: ")
    phone = input("Telefon numarası: ")
    address = input("Adres: ")
    
    members = load_members()
    existing_ids = [m['member_id'] for m in members]
    next_id = max(existing_ids, default=0) + 1

=======
def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []
    
def save_members(members):
    with open("members.json", 'w', encoding='utf-8') as f:
        json.dump(members, f, indent=4, ensure_ascii=False)      

def add_member(name, phone, address):
    name = input("Üye adı: ")
    phone = input("Telefon numarası: ")
    address = input("Adres: ")
    
    members = load_members()
    existing_ids = [m['member_id'] for m in members]
    next_id = max(existing_ids, default=0) + 1

>>>>>>> Stashed changes
    new_member = {
        "member_id": next_id,
        "name": name,
        "phone": phone,
        "address": address
    }
    members.append(new_member)
    save_members(members)
    print(f"\n{new_member['name']} adlı üye başarıyla eklendi. (ID: {new_member['member_id']})")
                  
def delete_member(member_id):
    try:
        member_id = int(input("Silinecek üyenin ID'sini girin: "))
    except ValueError:
        print("Geçersiz ID. Lütfen sayısal bir değer giriniz.")
        return
    
    members = load_members()
    member = next((m for m in members if m['member_id'] == member_id), None)
    if member:
        members.remove(member)
        save_members(members)
        print(f"{member['name']} adlı üye başarıyla silindi.")
    else:
        print("Üye Bulunamadı.")

def search_member(search_term):
    search_term = input("Aranacak kelime(isim, telefon, adres): ").lower()
    members = load_members()

    result = [
        m for m in members
        if search_term in str(m['name']).lower()
        or search_term in str(m['phone']).lower()
        or search_term in str(m['address']).lower()
        or search_term == str(m["member_id"])
    ]

    if result:
        print("\n Arama sonuçları: ")
        for m in result:
            print(f"[ID {m['member_id']}] {m['name']} | {m['phone']} | {m['address']}")
    else:
        print("Eşleşen üye bulunamadı.")
    

def get_all_members():
    return load_members()

def show_members():
    members = load_members()
    if not members:
        print("Kayıtlı üye yok.")
        return
    print("\n Tüm üyeler: ")
    for m in members:
        print(f"[ID {m["member_id"]} {m['name']} | {m['phone']} | {m['address']}]")
    

def update_member(member_id, field, new_value):

    try:
        member_id = int(input("GÜncellenecek Üyenin ID'sini Giriniz: "))
    except ValueError:
        print("Geçersiz ID.")
        return
    print("\nGüncellenecek alanı seçin:")
    print("1 - İsim")
    print("2 - Telefon")
    print("3 - Adres")
    chois = input("Seçiminiz 1/2/3: ")
<<<<<<< Updated upstream
=======

    field_map = {
        "1": "name",
        "2": "phone",
        "3": "address"
    }    

    if chois not in field_map:
        print("Geçersiz Seçim.")
        return

    field = field_map[chois]
    new_value = input(f"Yeni {field}: ")

    members = load_members()
    for m in members():
        if m[member_id] == member_id:
            m[field] = new_value
            save_members(members)
            print(f"Üye {field} Bilgisi {new_value} olarak Güncellendi.") 
            return
    print("Üye Bulunamadı.")   

def member_exists(member_id):       
    
    

>>>>>>> Stashed changes

    field_map = {
        "1": "name",
        "2": "phone",
        "3": "address"
    }    

    if chois not in field_map:
        print("Geçersiz Seçim.")
        return

    field = field_map[chois]
    new_value = input(f"Yeni {field}: ")

    members = load_members()
    for m in members():
        if m[member_id] == member_id:
            m[field] = new_value
            save_members(members)
            print(f"Üye {field} Bilgisi {new_value} olarak Güncellendi.") 
            return
    print("Üye Bulunamadı.")   

def member_exists(member_id):       
    

def save_tracking():
    """save updates to tracking.json file"""

def get_tracking():
    """load tracking data from tracking.json file"""

def lend_book(member_id, book_barcode, loan_date, return_date):
    """Process book loan to a member"""
    pass

def return_book(member_id, book_barcode):
    """Process book return from a member"""
    pass

def get_loan_history(member_id=None):
    """Retrieve loan history (all or for specific member)"""
    pass

def get_overdue_loans():
    """Identify books that are overdue"""
    pass

def update_loan_status(loan_id, status):
    """Update the status of a loan"""
    pass