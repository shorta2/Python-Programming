#!/usr/bin/env python3

import sqlite3
from contextlib import closing

conn = None

# Connect to the SQLite database

def connect():
    """Connect to the SQLite database or create it if it doesn't exist."""
    global conn
    if not conn:
        DB_FILE = "books_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

# Create the table for storing books

def create_tables():
    """Create the Books table if it doesn't already exist."""
    query = '''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            page_number INTEGER NOT NULL,
            progress_status TEXT NOT NULL,
            rating REAL,
            genre TEXT,
            date_added TEXT
        )
    '''
    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()

# Fetch all books from the database

def get_all_books():
    """Fetch all books from the database."""
    query = '''SELECT id, title, author, page_number, progress_status, rating, genre, date_added
               FROM Books
               ORDER BY title'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        rows = c.fetchall()

        books = []
        for row in rows:
            books.append(dict(row))
        return books

# Fetch a single book by its ID

def get_book_by_id(book_id):
    """Fetch a single book by its ID."""
    query = '''SELECT id, title, author, page_number, progress_status, rating, genre, date_added
               FROM Books
               WHERE id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        row = c.fetchone()
        return dict(row) if row else None

# Add a new book to the database

def add_book(title, author, page_number, progress_status, rating, genre, date_added):
    """Add a new book to the database."""
    sql = '''INSERT INTO Books (title, author, page_number, progress_status, rating, genre, date_added)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (title, author, page_number, progress_status, rating, genre, date_added))
        conn.commit()

# Update a specific field of a book

def update_book(book_id, field, value):
    """Update a specific field of a book."""
    sql = f'''UPDATE Books
              SET {field} = ?
              WHERE id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (value, book_id))
        conn.commit()

# Delete a book from the database

def delete_book(book_id):
    """Delete a book from the database."""
    sql = '''DELETE FROM Books
             WHERE id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book_id,))
        conn.commit()

# Close the database connection

def close():
    """Close the database connection."""
    if conn:
        conn.close()
