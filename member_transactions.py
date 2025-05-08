import os
import json
import core.time_utils as tu
import core.data_io

def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", "r", encoding= 'udf-8') as f:
            return json.load(f)
    except:
        return []
def save_members(member):
    with open("members.json", 'w', encoding= 'udf-8') as f:
        json.dump(member, f, indent=4, ensure_ascii=False)

def add_member(name, phone, address):
    members = load_members()
    existing_id = [m['member_id'] for m in members]
    next_id = max(existing_id, default=0) + 1

    new_member = {
        'member_id': next_id,
        'name': name,
        'phone': phone,
        'address': address,
    }

    members.append(new_member)
    save_members(members)
    print(f"{new_member['name']} adlı üye başarıyla eklendi. (ID: {new_member['member_id']})")

def delete_member(member_id):
    members = load_members()
    member = next(m for m in members if m['member_id' == member_id, None])
    if member:
        members.remove(member)
        save_members(members)
        print(f"{member['name']} adlı üye başarıyla silindi.")
    else:
        print("Üye Bulunamadı.")

def search_member(search_term):
    members = load_members()

    result = [
        m for m in members
        if search_term in str(m['name']).lower()
        or search_term in str(m['phone']).lower()
        or search_term in str(m['address']).lower()
        or search_term in (m['member_id'])
    ]

    if result:
        print("\n Arama Sonuçları: ")
        for m in result:
            print(f"ID: {m['member_id']}")
            print(f"İSİM: {m['name']}")
            print(f"Telefon: {m['phone']}")
            print(f"adres: {m['address']}")
        else:
            print("Eşleşen üye bulunamadı.")

def get_all_members():
    return load_members

def member_exists(member_id):
    members = load_members()
    return any(m['member_id'] == member_id for m  in members)

def lend_book(member_id, book_barcode, loan_date, return_date):
    """Process book loan to a member"""
    pass

def return_book(member_id, book_barcode):
    """Process book return from a member"""
    pass