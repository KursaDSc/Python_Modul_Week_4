import os
import json

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Merkezi hata kontrol rutini
def handle_errors(error):
    if isinstance(error, ValueError):
        print("Lütfen geçerli bir sayı giriniz!")
    else:
        print(f"Beklenmeyen bir hata oluştu: {error}")

# Süreclerle ilgili durum bildirimi
def show_message(message):
    print(message)
    input("\nDevam etmek için bir tuşa basın...")