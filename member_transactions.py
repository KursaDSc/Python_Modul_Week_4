import os
import json
import datetime
import core.time_utils as tu
import core.data_io as io

def load_members():
    if not os.path.exists("members.json"):
        return []
    try:
        with open("members.json", "r", encoding='udf-8') as f:
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
    member = next((m for m in members if m['member_id'] == member_id), None)
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
        or str(search_term) == str(m['member_id'])
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
    return load_members()

def member_exists(member_id):
    members = load_members()
    return any(m['member_id'] == member_id for m  in members)

def lend_book(member_id, book_barcode):
    if not member_exists(member_id):
        print("Üye Bulunamadı.")
        return
    
    books = io.read_json("books.json") #data.io klasötünden fonksiyon ile kitap bilgileri okumalı(kontrol et!)
    book = next((b for b in books if b['barcode'] == book_barcode and b['satus'] == 'available'), None)
    if not book:
        print("Kitap mevcut değil ya da ödünç verilmiş.")
        return
    
    tracking = io.read_json("tracking.json") #data.io klasötünden fonksiyon ile tracking bilgileri okumalı(kontrol et!)

    loan_id = f"L{len(tracking) + 1:03d}"
    registration_date = datetime.datetime.now()
    return_date = tu.calculate_due_date(registration_date).strftime("%Y-%m-%d") #burda diğer dosyadan veriyi doğru almıyor olabilir.

    loan_record = {
        'loan_id': loan_id,
        'member_id': member_id,
        'book_barcode': book_barcode,
        'registration_date': registiration_date.strftime("%Y-%m-%d"),
        'return_date': return_date
    }

    tracking.append(loan_record) #append renksiz?
    io.write_json("tracking.json", tracking) #paratez içerisindekine tırnak işareti ve içersiindeki bölğme gerek var mı?

    book["status"] = "borrowed"
    io.write_json("books.json", books)

    print(f"{book['title']} adlı kitap {loan_record['registration_date']} tarihinde ödünç verildi. "
          f"Teslim tarihi: {return_date}")

def return_book(member_id, book_barcode):
    tracking = io.read_json("tracking.json")
    books = io.read_json("books.json")

    loan_record = next((l for l in tracking if l['member_id' == member_id and l['barcode'] == book_barcode]), None)

    if not loan_record:
        print("Bu kitap, bu üye tarafından ödünç alınmamış.")
        return
    
    book = next((b for b in books if b['barcode'] == book_barcode), None)
    if book:
        book['status'] = "available"  
        io.write_json("books.json", books)
    
    tracking.remove(loan_record)
    io.write_json("tracking.json", tracking)
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{book['title']} adlı kitap {loan_record['registration_date']} tarihinde ödünç alındı. "
        f"{now_str} itibariyle iade alındı ve kitap 'available' durumuna getirildi.")

    