# Library Management System (OOP)

## Project Overview
This project implements a simple library management system using Python OOP.  
It manages books, members, and borrowing transactions, allowing users to add, borrow, return, and view books.

## Project Structure


## Design Overview

### Book
Attributes: `id`, `title`, `author`, `total_copies`, `available_copies`  
Methods:  
- `borrow_copy()` decreases available copies  
- `return_copy()` increases available copies  

### Member
Attributes: `id`, `name`, `email`, `borrowed_books`  
Methods:  
- `borrow_book(book)` allows borrowing up to 3 books  
- `return_book(book)` returns a borrowed book  

### Library
Attributes: `books`, `members`, `borrowed_books`  
Methods:  
- `add_book()`, `add_member()`  
- `find_book()`, `find_member()`  
- `borrow_book()`, `return_book()`  
- `display_available_books()`, `display_member_books()`

## Testing
Test file: `test_library_oop.py`

Covers:
- Adding books and members  
- Borrowing and returning books  
- Displaying information  
- Edge cases: unavailable books, borrow limit, invalid returns, missing members/books  

## How to Run
Place all files in the same folder and run:
