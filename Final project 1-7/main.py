from BookTracker_package import CRUD as c
from BookTracker_package import statistics as s

book_list={}
book_auto_id = 1

def main():
    msg="""
    Choose an operation:
    1 - abb a new book to the book list
    2 - show the book list
    3 - change book status
    4 - delete the book
    5 - show statiscs: count books by status
    6 - show statiscs: count read pages
    0 - exit from program 
    
    """
    operation=input(msg)
    while operation != "0":
        match operation:
            case "1":
                c.add_book()
            case "2":
                c.show_books()
            case "3":
                c.update_book()
            case "4":
                c.delete_book()
            case "5":
                s.count_books_by_status()
            case "6":
                s.count_total_pages_read()
            case _:
                print("Didn't get!")
        operation=input(msg)


main()
