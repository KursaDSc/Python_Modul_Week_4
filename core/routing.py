from core.utils import *
import member_transactions as mt
import book_transactions as bt

# ortak fonksiyon
def route_operation(choice, operation_map):
    func = operation_map.get(choice)
    if func:
        func()
    else:
        show_message("Geçersiz işlem!")

# üye menüsü yönlendirme
def route_member_operation(choice):
    member_ops = {
        1: mt.show_members,
        2: mt.add_member,
        3: mt.search_member,
        4: mt.delete_member,
        5: mt.lend_book,
        6: mt.return_book,
        7: mt.get_loan_history,
        0: None
    }
    clear_screen()
    route_operation(choice, member_ops)

# Kitap menüsü yönlendirme
def route_book_operation(choice):
    book_ops = {
        1: bt.get_all_books,
        2: bt.add_book,
        3: bt.search_book,
        4: bt.delete_book,
        5: bt.is_book_available,  # isteğe bağlı
        0: None
    }
    clear_screen()  
    route_operation(choice, book_ops)