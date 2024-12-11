#!/usr/bin/env python3

from db import connect, create_tables, add_book, get_all_books, get_book_by_id, update_book, delete_book, close
from datetime import datetime

def display_menu():
    print("\n--- Book Rating Tracker ---")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. View a specific book")
    print("6. Exit")

def view_all_books():
    books = get_all_books()
    if not books:
        print("\nNo books found in the database.")
    else:
        print("\nBooks in the database:")
        print(f"{'ID':<5}{'Title':<30}{'Author':<20}{'Rating':<10}{'Progress':<15}")
        print("-" * 80)
        for book in books:
            print(f"{book['id']:<5}{book['title']:<30}{book['author']:<20}{book['rating']:<10}{book['progress_status']:<15}")

def add_new_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author name: ").strip()
    page_number = int(input("Enter the total number of pages: ").strip())
    progress_status = input("Enter the progress status (Not Started/In Progress/Completed): ").strip()
    rating = float(input("Enter your rating (1-5): ").strip())
    genre = input("Enter the genre: ").strip()
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    add_book(title, author, page_number, progress_status, rating, genre, date_added)
    print(f"\nBook '{title}' added successfully!")

def update_existing_book():
    book_id = int(input("Enter the ID of the book to update: ").strip())
    book = get_book_by_id(book_id)
    if not book:
        print("\nBook not found.")
        return

    print(f"\nCurrent details of book ID {book_id}:")
    print(book)
    field = input("Enter the field to update (title, author, page_number, progress_status, rating, genre): ").strip()
    value = input("Enter the new value: ").strip()

    # Convert numeric fields to appropriate types
    if field in ['page_number']:
        value = int(value)
    elif field in ['rating']:
        value = float(value)

    update_book(book_id, field, value)
    print(f"\nBook ID {book_id} updated successfully!")

def delete_existing_book():
    book_id = int(input("Enter the ID of the book to delete: ").strip())
    book = get_book_by_id(book_id)
    if not book:
        print("\nBook not found.")
        return

    delete_book(book_id)
    print(f"\nBook ID {book_id} deleted successfully!")

def view_specific_book():
    book_id = int(input("Enter the ID of the book to view: ").strip())
    book = get_book_by_id(book_id)
    if not book:
        print("\nBook not found.")
    else:
        print("\nBook Details:")
        for key, value in book.items():
            print(f"{key}: {value}")

def main():
    connect()
    create_tables()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            view_all_books()
        elif choice == '2':
            add_new_book()
        elif choice == '3':
            update_existing_book()
        elif choice == '4':
            delete_existing_book()
        elif choice == '5':
            view_specific_book()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    close()

if __name__ == "__main__":
    main()
