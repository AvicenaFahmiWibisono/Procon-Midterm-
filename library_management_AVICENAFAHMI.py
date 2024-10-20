
# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"  # Reset to default color

#𝐒𝐈𝐒𝐓𝐄𝐌 𝐌𝐀𝐍𝐀𝐉𝐄𝐌𝐄𝐍 𝐏𝐄𝐑𝐏𝐔𝐒𝐓𝐀𝐊𝐀𝐀𝐍
# Description
# This system create a library management system that allows users to:

#1. Add books to the library.
#2. Search for books by category or author.
#3. Borrow and return books.
#4. Display a list of available books.

#The system will use functions to separate logic, looping to display interactive menus, and apply OOP principles such as encapsulation, polymorphism, and inheritance.

class Book:
    """
    1. Class Book
    
    Contains information about the book, such as title, author,and availability status (borrowed or available).
    Encapsulation is used here to protect the book attributes from direct access.
    """
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def borrow_book(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def is_borrowed(self):
        return self.__is_borrowed


class Library:
    
    """
    2. Class Library (Inheritance)
    The Library class is a place to store book collections and provides functions for adding books, searching for books, and borrowing and returning books.
    Inheritance can be used to extend the functionality of Library. For example, we can create a DigitalLibrary that may store ebooks.
    """
    
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book.get_author().lower() == author.lower()]

    def display_books(self):
        if not self.books:
            print("Tidak ada buku yang tersedia.")
        for book in self.books:
            status = 'Dipinjam' if book.is_borrowed() else 'Tersedia'
            print(f"{book.get_title()} oleh {book.get_author()} - {status}")


def borrow_or_return_book(library, title, action):
    
    """
    3. Polymorphism in Action
    Polymorphism can be applied to borrowing a book or returning a book, where the Book object can respond to the same
    command with different results (borrowed or returned).
    """
    
    for book in library.books:
        if book.get_title().lower() == title.lower():
            if action == "borrow":
                if book.borrow_book():
                    print(f"{GREEN}Buku '{title}' berhasil dipinjam.{RESET}")
                else:
                    print(f"{YELLOW}Buku '{title}' sudah dipinjam.{RESET}")
            elif action == "return":
                if book.return_book():
                    print(f"{GREEN}Buku '{title}' berhasil dikembalikan.{RESET}")
                else:
                    print(f"Buku '{title}' tidak sedang dipinjam.")
            return
    print(f"Buku '{title}' tidak ditemukan.")

banner = f"""
  {BLUE}
  
██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝     ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
PresUniv                                                                                                              by Avicena Fahmi (012202405002)                     
{RESET} """

print(banner)

def main_menu():
    
    """
    4. Interactive Menu (Selection and Repetition)
    Use an if-else or while-loop structure to provide an interactive menu for users to select actions such as adding books, borrowing, or returning books.
    
    - Selection: if-else is used in the main menu to select an action based on user input.
    - Repetition: while-loops ensure the menu continues to run until the user chooses to exit.
    """
    
    library = Library()

    while True:
        print("\n")
        print("1. Tambah Buku")
        print("2. Cari Buku Berdasarkan Penulis")
        print("3. Tampilkan Semua Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Keluar")

        choice = input("Pilih opsi: ").strip()

        if choice == '1':
            title = input("Masukkan judul buku: ").strip()
            author = input("Masukkan penulis: ").strip()
            if title and author:
                library.add_book(Book(title, author))
                print(f"{GREEN}Buku '{title}' oleh {author} berhasil ditambahkan.{RESET}")
            else:
                print("Judul dan penulis tidak boleh kosong.")
        elif choice == '2':
            author = input("Masukkan nama penulis: ").strip()
            results = library.search_by_author(author)
            if results:
                for book in results:
                    print(f"- {book.get_title()} oleh {book.get_author()}")
            else:
                print(f"Tidak ada buku yang ditemukan untuk penulis '{author}'.")
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            title = input("Masukkan judul buku yang ingin dipinjam: ").strip()
            borrow_or_return_book(library, title, "borrow")
        elif choice == '5':
            title = input("Masukkan judul buku yang ingin dikembalikan: ").strip()
            borrow_or_return_book(library, title, "return")
        elif choice == '6':
            print(f"{GREEN}Terima kasih telah menggunakan sistem perpustakaan.{RESET}")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main_menu()

    """
    𝐂𝐨𝐧𝐜𝐞𝐩𝐭 𝐄𝐱𝐩𝐥𝐚𝐧𝐚𝐭𝐢𝐨𝐧
    •Function: Each feature (such as add book, borrow, return) is placed in a separate function for modularity.
    •Encapsulation: Book attributes are protected with getter and setter methods inside the Book class.
    •Polymorphism: The borrow_or_return_book function exhibits polymorphism, where the book object can respond in different ways depending on whether the book is borrowed or returned.
    •Inheritance: Can be further extended if there are variations of the library, e.g. DigitalLibrary for ebooks.
    """
    