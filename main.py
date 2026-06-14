from database.book_db import BookDB
from database.base_models import CreateBook, Genre

book = BookDB()
new_book = CreateBook(title="a", author="b", genre=Genre('Non-Fiction'))
book.create_book(new_book)
book.get_all_books()
count = book.count_active_borrows_by_member(1)
print(count)
