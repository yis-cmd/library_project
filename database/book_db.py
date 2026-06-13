from database.base_models import Book, CreateBook, InsertBook
from database.engine import Engine


class BookDB:
    def __init__(self) -> None:
        self.table_name = "books"
        self.engine = Engine()

    def create_book(self, data:CreateBook):
        book = InsertBook.model_validate(data.model_dump())
        self.engine.insert(self.table_name, book.model_dump())

    def get_all_books(self):
        pass

    def get_book_by_id(self, id):
        pass

    def update_book(self, id, data):
        pass

    def set_available(self, id, val, member_id):
        pass

    def count_total_books(self):
        pass

    def count_available_books(self):
        pass

    def count_borrowed_books(self):
        pass

    def count_by_genre(self):
        pass

    def count_active_borrows_by_member(self, member_id):
        pass

