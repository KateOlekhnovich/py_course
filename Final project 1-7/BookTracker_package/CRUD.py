book_list = {}
book_auto_id = 1

def add_book():
    """This function adds a new book to the book list. 
    
    Arguments:
    No external arguments. All data is entered through input().
    
    
    True - if a book has been successfully added to the list
    """
    global book_auto_id
    print ("Put details about the book you are going to add to the book list!")
    b_name = input("Book Title: ").strip().title()
    b_author = input("Book Author: ").strip().title()
    b_page = int(input ("Page Quantity: "))
    book_list[book_auto_id] = { 
        "book_title":b_name, 
        "book_author":b_author, 
        "N pages":b_page, 
        "status": "Want to read"
    }
    print(f"'{b_name}' has been added to the list with ID {book_auto_id}")
    book_auto_id +=1
    return True


def show_books():
    """This function shows the book list.
   
    Arguments:
    No external arguments.
    
    Returns:
    None. This function simply prints the list of books to the screen."""
    if not book_list:
        print("No books in the list.")
        return
    print ("Show book list")
    for book_id, description in book_list.items():
        print("______________")
        print(f"Book id:{book_id}")
        for key, value in description.items():
            print("\t", key, ":", value)
        print("______________")


def update_book():
    """This function allows an user to update the status of the book. 
    
    Arguments:
    No external arguments. The book's ID is entered through input().
    
    Returns:
    False  - if the book with the given ID is not found in the list.
    The function doesn't return anything but prints a message confirming the status update.
    """
    book_id=int(input("Put book id: "))
    if book_id not in book_list:
        print (f"The {book_id} is not the list.")
        return False
    inside = book_list.get(book_id)
    inside ['status'] = input ("Choose status: Read (D) or Reading (R) ---> ")
    if inside ['status'] == "D" or inside ['status'] == "d":
        inside['status'] = "Read"
        book_list.update({book_id:inside})
        print (f"Status has been changed to '{inside['status']}' for the book with ID: {book_id}")
    elif inside['status'] == "R" or inside['status'] == "r":
        inside['status'] = "Reading"
        book_list.update({book_id:inside})
        print (f"Status has been changed to '{inside['status']}' for the book with ID: {book_id}")
    else:
        print("Didn't get you!")

 
def delete_book():
    """This function deletes the book.
    
    Arguments: 
    No external arguments. The book's ID is entered through input().
    
    Returns:
    True - if the ook has been successfully deleted from the list
    False - if the book was not found."""
    book_id=int(input("Put book id: "))
    
    if not book_list:
        print("No books in the list.")
        return False
    
    if book_id in book_list:
        del book_list[book_id]
        print("______________")
        print(f"Book id:{book_id} has been removed from the book list")
        print("______________")
        return True
    else:
        print (f"Book id:{book_id} ia not found in the book list")
        return False


if __name__== "__main__":
    print ("CRUD.py запущен по F5 или вручную")
    print ()
    test_data="testdata"
    add_book()
    add_book()
    show_books()
    delete_book()
    show_books()
else:
    print ("CRUD.py запущен через импорт в другой моуль")
