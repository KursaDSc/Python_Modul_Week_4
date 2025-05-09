import json
import core.data_io as do 


# JSON dosyasını yükleme işlemi
def load_tracking_data():
    return do.read_json('data/tracking.json')
   
# JSON dosyasına veri kaydetme işlemi
def save_tracking_data(data):
    do.write_json('data/tracking.json', data)

def add_record(record):
    data = load_tracking_data()    
    data.append(record)    
    save_tracking_data(data)

def delete_record(barkod):
    data= load_tracking_data()   # Mevcut verileri yukle
    updated_data = [record for record in data if record['barcode'] != barkod]   # Barkodu eşleşmeyen kayıtları tutarak diğerini siliyrz
    save_tracking_data(updated_data)  # Güncellenmiş veriyi kaydet
    
def track_loan(member_id):
    data = load_tracking_data()  # JSON dosyasındaki ödünç kitap verilerini yükle

    # Bu satır, member_id'si verilen kişinin hâlâ iade etmediği kitapları filtreler.
    # Yani return_date alanı boş olan (geri verilmemiş) kitaplar
    active_loans = [
        record for record in data
        if record.get('member_id') == int(member_id)
    ]

    return active_loans  # Bu fonksiyon, üyenin iade etmediği kitapları geri döner (liste olarak)