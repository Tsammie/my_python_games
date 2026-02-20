# You are tasked with developing a simple Library Management System using Python and SQLite. The system should allow the 
# library staff to perform the following operations:

# Add a Book to the Library:
# The staff should be able to add new books to the library's collection. Each book should have a title, author, genre, and the year of publication.
# The database should automatically assign a unique Book ID to each book.


# Search for a Book:
# The staff should be able to search for books based on the following criteria:
# By title
# By author
# By genre
# The system should return a list of books that match the search criteria.


# Check Out a Book:
# The system should allow the staff to record when a book is checked out. For each checkout, the system should record the Book ID, Member ID, and the checkout date.
# The system should ensure that a book can only be checked out if it is available in the library (i.e., not already checked out).


# Return a Book:
# The system should allow the staff to record when a book is returned. For each return, the system should update the record to indicate that the book is now available.


# View All Books:
# The staff should be able to view a list of all books in the library, including details such as title, author, genre, year of publication, and availability status (whether the book is checked out or available).

# REQUIREMENTS:

# Database Schema:
# Design a database schema to support the operations mentioned above. Your schema should include tables for Books, Members, and Checkouts.


# Python Implementation:
# Write Python functions to perform each of the operations described above. Each function should interact with the SQLite database to read from or write to the tables.


# User Interface:
# Develop a simple command-line interface that allows the staff to perform the operations. The interface should display menus and prompts for user input.

# Deliverables:
# - A Python script (library_management_system.py) containing the complete implementation.

import sqlite3

conn = sqlite3.connect("Library.db")

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE if not exists Book(
Book_ID Integer PRIMARY KEY autoincrement,
Title TEXT NOT NULL UNIQUE,
Author TEXT NOT NULL,
genre text not null, 
year_of_publication int not null)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Members(
Member ID Integer PRIMARY KEY,
Name TEXT NOT NULL,
Age int NOT NULL)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Checkouts1(
Date TEXT not null)
"""
)

def add_book():
    title = input('Please enter the title of the book : ')
    author = input('Please enter the author of the book : ')
    yop = int(input('Please enter the year of publication : '))
    genre = input('Please enter the genre : ')
    
    try:
        cursor.execute("""
            INSERT INTO book (Title, Author, genre,year_of_publication) VALUES
            (?, ?, ?, ?)
            """,(title,author,genre,yop))
    except sqlite3.IntegrityError:
        print("Book already exist!!")
    else:
        conn.commit()

add_book()