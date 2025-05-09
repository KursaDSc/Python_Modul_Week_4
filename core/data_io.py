import json
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
    data = read_json_file(filepath)
    if isinstance(data, list):
        data.append(new_data)
    else:
        data = [new_data]
    write_json_file(filepath, data)
    
