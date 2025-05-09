import json
import os

#Json dosayasini oku
def read_json(filepath):
    if not os.path.exists(filepath):
        return []  # Dosya yoksa boş liste döndür
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # JSON hataliysa boş liste döndür

#json dosyasina yaz
def write_json(filepath, data):
     with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# JSON dosyasına veri ekle (liste yapısında ise)
def append_to_json_file(filepath, new_data):
    data = read_json(filepath)
    if isinstance(data, list):
        data.append(new_data)
    else:
        data = [new_data]
    write_json(filepath, data)

# Belirli bir öğeyi (kimlik,tbaslik, isim vs.) sil (liste içindeki sözlük)
#chatgpt`den buldum
def delete_from_json_file(filepath, key, value):
    data = read_json(filepath)
    if isinstance(data, list):
        data = [item for item in data if item.get(key) != value]
        write_json(filepath, data)

# Belirli bir öğeyi güncelle (liste içindeki sözlük)
def update_json_item(filepath, key, value, updated_item):
    data = read_json(filepath)
    if isinstance(data, list):
        for i, item in enumerate(data):
            if item.get(key) == value:
                data[i] = updated_item
                break
        write_json(filepath, data)

# Belirli öğeyi bul (tek eşleşme bekleniyorsa)
def find_in_json(filepath, key, value):
    data = read_json(filepath)
    if isinstance(data, list):
        for item in data:
            if item.get(key) == value:
                return item
    return None

# Tüm eşleşmeleri döndür (filtreleme)
def filter_json_items(filepath, key, value):
    data = read_json(filepath)
    if isinstance(data, list):
        return [item for item in data if item.get(key) == value]
    return []

    
