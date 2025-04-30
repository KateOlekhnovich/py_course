from BookTracker_package import CRUD

def count_books_by_status():
    """This function shows how many books in each status of the book list. 
    
    Arguments:
    No external arguments.

    Returns:
    The function doesn't return anything but prints the statistics to the screen.
    """
    if not CRUD.book_list:
        print("No books in the list.")
        return
    status_count = {"Want to read": 0, "Reading": 0, "Read": 0}
    
    for book in CRUD.book_list.values():
        status = book.get ("status")
        if status in status_count:
            status_count[status] += 1
    print ("Statistics by status")
    for status, count in status_count.items():
        print (f" - {status}: {count} book(s)")
        
def count_total_pages_read():
    """ This function counts and displays the total number of pages read. 
    It only considers books with the "Read" status. 
    
    Arguments:
    No external arguments.

    Returns:
    The function doesn't return anything but prints the total number of pages read.
    """
    total_pages = 0
    for book in CRUD.book_list.values():
        if book.get('status') == "Read":
            total_pages += book.get("N pages")
    print(f" Total read pages: {total_pages}")
    

if __name__== "__main__":
    print ("statistics.py запущен по F5 или вручную")
    print ()
else:
    print ("statistics.py запущен через импорт в другой моуль")
    