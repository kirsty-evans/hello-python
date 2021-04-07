import book
import author  # importing classes book and author

first_author = author.Author(
    "John", "Doe", "USA"
)  # passing name, first name and nationality from author.py
book = book.Book("All about Python", 1, author)  # passing title, revision and author

book.lend("testUser")