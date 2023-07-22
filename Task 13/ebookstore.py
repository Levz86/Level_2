import sqlite3

#creates a table with the given information
def create_table():
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE books(book_id INTEGER PRIMARY KEY,
                        title varchar(255) NOT NULL, 
                        author varchar(255) NOT NULL, 
                        qty INTEGER NOT NULL)''')
    
        # add the infomarion to the table
        cursor.execute("INSERT INTO books VALUES(3001, 'A Tale of Two Cities', 'Charles Dickens', 30)")
        cursor.execute("INSERT INTO books VALUES(3002, 'Harry Potter and the Philosophers Stone', 'J.K Rowling', 40)")
        cursor.execute("INSERT INTO books VALUES(3003, 'The Lion, the Witch and the Wardrobe', 'C.S Lewis', 25)")
        cursor.execute("INSERT INTO books VALUES(3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)")
        cursor.execute("INSERT INTO books VALUES(3005, 'Alice in Wonderland', 'Lewis Carrol', 12)")
    
        db.commit()
    except Exception as e:
        db.rollback()

        cursor.close()

#to add a new book to the table
def new_book():
    
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
                
    # askes user to enter information about book
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    qty = (input('Enter the quantity of the book: '))

    #adds the book to the table
    cursor.execute('INSERT INTO books (title, author, qty) values (?, ?, ?)', (title, author, qty))
       
    print("New book has been added")
    db.commit()

#to update a book detail
def update_book():
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
    
    #asks user to enter information  about the updated book
    book_id = int(input('Enter book ID to update: '))
    title = input("Enter new book title (leave blank to keep current title): ")
    author = input("Enter new book author (leave blank to keep current author): ")
    qty = input("Enter new book quantity (leave blank to keep current quantity): ")
        
    #add the update to the table
    cursor.execute('SELECT * FROM books WHERE book_id=?', (book_id,))
    book = cursor.fetchone()
    if not book :
        print("Book not found!")
        return
    if title.strip():
        cursor.execute("UPDATE books SET title=? WHERE book_id=?", (title, book_id))
    if author.strip():
        cursor.execute("UPDATE books SET author=? WHERE book_id=?", (author, book_id))
    if qty.strip():
        cursor.execute("UPDATE books SET qty=? WHERE book_id=?", (qty, book_id))
        
    print("Book has been updated")
    db.commit()

#to delete a book
def delete_book():
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
   
    #asks user information about the book to be deleted
    book_id = int(input('Enter book ID to delete: '))
    title = input('Enter the title of the book to delete: ')

    cursor.execute("SELECT * FROM books WHERE book_id=? AND title=?", (book_id, title))
    book = cursor.fetchone()
    if not book:
        print("Book not found!")
        return

    cursor.execute('DELETE FROM books WHERE book_id=? AND title=?', (book_id, title))
    print("Book has been deleted")
    db.commit()

#searchs for a book
def search_book():
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()

    #askes user for the title of the book to search for
    title = input('Enter the title of the book to search: ')

    cursor.execute('SELECT * FROM books WHERE title=?', (title,))
    books = cursor.fetchall()
    if not books:
        print("Book not found!")
        return
    for book in books:
        print(f"{book[0]} {book[1]} {book[2]} {book[3]}")
    
    db.commit()
    cursor.close()  

#creats the menu options
def menu():
    print('''
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit''')

    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchall()
    for row in result:
        print(row, "/n")


    user_input = input("Enter a choice: ")
    return user_input


if __name__ == "__main__":
    create_table()
    while True:
        choice = menu()
        if choice == "1":
            new_book()            
        elif choice =="2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again")






