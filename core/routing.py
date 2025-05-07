from core.utils import *
import core.member_handlers as mh
import core.book_handlers as bh

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
        1: mh.handle_show_members,
        2: mh.handle_add_member,
        3: mh.handle_search_member,
        4: mh.handle_delete_member,
        5: mh.handle_loan_book,
        6: mh.handle_return_book,
        7: mh.handle_book_tracking,
        0: None
    }
    clear_screen()
    route_operation(choice, member_ops)

# Kitap menüsü yönlendirme
def route_book_operation(choice):
    book_ops = {
        1: bh.handle_show_books,
        2: bh.handle_add_book,
        3: bh.handle_search_book,
        4: bh.handle_delete_book,
        0: None
    }
    clear_screen()  
    route_operation(choice, book_ops)