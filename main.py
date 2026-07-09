import csv
import os

BOOKS_FILE = "books.csv"

# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Book ID", "Book Name", "Author", "Status"])

# Add Book
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(BOOKS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, book_name, author, "Available"])

    print("\nBook Added Successfully!\n")

# View Books
def view_books():
    print("\n========== BOOK LIST ==========")

    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<10} {:<30} {:<20} {:<10}".format(*row))

# Search Book
def search_book():
    search = input("Enter Book ID or Book Name: ").lower()
    found = False

    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if search == row[0].lower() or search == row[1].lower():
                print("\nBook Found")
                print("-------------------------------")
                print("Book ID :", row[0])
                print("Book Name :", row[1])
                print("Author :", row[2])
                print("Status :", row[3])
                found = True

    if not found:
        print("Book Not Found!")

# Issue Book
def issue_book():
    book_id = input("Enter Book ID to Issue: ")

    books = []
    issued = False

    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == book_id and row[3] == "Available":
                row[3] = "Issued"
                issued = True
            books.append(row)

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    if issued:
        print("Book Issued Successfully!")
    else:
        print("Book Not Available!")

# Return Book
def return_book():
    book_id = input("Enter Book ID to Return: ")

    books = []
    returned = False

    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == book_id and row[3] == "Issued":
                row[3] = "Available"
                returned = True
            books.append(row)

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    if returned:
        print("Book Returned Successfully!")
    else:
        print("Invalid Book ID!")

# Delete Book
def delete_book():
    book_id = input("Enter Book ID to Delete: ")

    books = []
    deleted = False

    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] != book_id:
                books.append(row)
            else:
                deleted = True

    with open(BOOKS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    if deleted:
        print("Book Deleted Successfully!")
    else:
        print("Book Not Found!")

# Main Menu
def menu():
    create_file()

    while True:
        print("\n===================================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("\nThank you for using Library Management System!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    menu()
