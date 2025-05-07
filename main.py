from core.utils import *
from core.menu import *
from core.routing import *

# Geçerli bir sayısal giriş yapılmasını sağlar.
def get_user_choice(message="Lütfen geçerli bir işlem numarası giriniz: "):
    while True:
        try:
            return  int(input(message))
        except Exception as e:
            handle_errors(e)

def run_member_menu():
    while True:
        display_members_menu()
        choice = get_user_choice()
        if choice == 0:
            break
        route_member_operation(choice)

def run_book_menu():
    while True:
        display_books_menu()
        choice = get_user_choice()
        if choice == 0:
            break
        route_book_operation(choice)


def main():
    while True:
        display_main_menu()
        choice = get_user_choice()
        if choice == 1:
            run_member_menu()
        elif choice == 2:
            run_book_menu()
        
        if choice == 0:
            print("Programdan çıkılıyor...")
            break

if __name__ == "__main__":
    main()  
