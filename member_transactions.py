import os
import json
import datetime
import core.time_utils as tu
import core.data_io as io
import tracking as tr


def add_member(name, phone, address):
    members = io.read_json('data/members.json')
    existing_id = [m['member_id'] for m in members]
    next_id = max(existing_id, default=0) + 1

    new_member = {
        'member_id': next_id,
        'name': name,
        'phone': phone,
        'address': address,
    }
    members.append(new_member)
    io.write_json('data/members.json', members)
    print(f"{new_member['name']} adlı üye başarıyla eklendi. (ID: {new_member['member_id']})")

def delete_member(member_id):
    members = io.read_json('members.json')
    member = next((m for m in members if m['member_id'] == member_id), None)
    if member:
        members.remove(member)
        io.write_json('data/members.json', members)
        print(f"{member['name']} adlı üye başarıyla silindi.")
    else:
        print("Üye Bulunamadı.")

def search_member(search_term):
    members = io.read_json('data/members.json')

    result = [
        m for m in members
        if search_term in str(m['name']).lower()
        or str(search_term) == str(m['member_id'])
    ]
    return result

def get_all_members():
    return io.read_json('data/members.json')

def member_exists(member_id):
    members = io.read_json('data/members.json')
    return any(m['member_id'] == int(member_id) for m in members)  # member_id'yi int() ile dönüştür


def lend_book(member_id, book_barcode):
    # Üye var mı kontrolü
    if not member_exists(member_id):
        print("Üye Bulunamadı.")
        return False

    # Kitapları oku
    books = io.read_json("data/books.json")
    
    # Kitap mevcut ve 'available' durumda mı kontrolü
    book = next((b for b in books if b['barcode'] == str(book_barcode) and b['status'] == 'available'), None)
    if not book:
        print("Kitap mevcut değil ya da ödünç verilmiş.")
        return False
    
    # Ödünç verme işlemi
    tracking = io.read_json("data/tracking.json")
    
    # Yeni loan_id oluştur
    loan_id = f"L{len(tracking) + 1:03d}"
    registration_date = datetime.datetime.now()
    return_date = tu.calculate_due_date(registration_date).strftime("%Y-%m-%d")  # Teslim tarihi hesaplama
    
    # Ödünç verme kaydını oluştur
    loan_record = {
        'loan_id': loan_id,
        'member_id': int(member_id),
        'barcode': int(book_barcode),
        'registration_date': registration_date.strftime("%Y-%m-%d"),
        'return_date': return_date
    }
    
    # Takip dosyasına ödünç verme kaydını ekle
    tracking.append(loan_record)
    io.write_json("data/tracking.json", tracking)

    # Kitap durumunu 'borrowed' olarak güncelle
    book["status"] = "borrowed"
    io.write_json("data/books.json", books)

    # Başarı mesajı
    print(f"{book['title']} adlı kitap {loan_record['registration_date']} tarihinde ödünç verildi. "
          f"Teslim tarihi: {return_date}")
    return True


def return_book(member_id, book_barcode):
    # Takip ve kitap dosyalarını oku
    tracking = io.read_json("data/tracking.json")
    books = io.read_json("data/books.json")
    
    # Ödünç alınan kitap kaydını bul
    loan_record = next(
        (l for l in tracking if int(l['member_id']) == int(member_id) and int(l['barcode']) == int(book_barcode)), 
        None
    )
    
    # Eğer ödünç alınmamışsa
    if not loan_record:
        print("Bu kitap, bu üye tarafından ödünç alınmamış.")
        return False
    
    # Kitap bilgilerini bul
    book = next((b for b in books if b['barcode'] == int(book_barcode)), None)
    
    # Kitap durumunu 'available' olarak güncelle
    if book:
        book['status'] = "available"
        io.write_json("data/books.json", books)

    # Takip kaydını sil
    tracking.remove(loan_record)
    io.write_json("data/tracking.json", tracking)

    # İade mesajı
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{book['title']} adlı kitap {loan_record['registration_date']} tarihinde ödünç alındı. "
          f"{now_str} itibariyle iade alındı ve kitap 'available' durumuna getirildi.")
    
    return True
    