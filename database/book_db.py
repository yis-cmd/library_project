from database.base_models import Book, CreateBook, InsertBook, UpdateBook
from database.engine import Engine


class BookDB:
    def __init__(self) -> None:
        self.table_name = "books"
        self.engine = Engine()
        self.create_table()

    def create_table(self):
        stmt = """
                CREATE TABLE IF NOT EXISTS `books` (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
                    is_available BOOLEAN NOT NULL DEFAULT TRUE,
                    borrowed_by_member_id INT NULL
                )
                """
        self.engine.create_table(stmt)

    def create_book(self, data: CreateBook):
        book = InsertBook.model_validate(data.model_dump())
        self.engine.insert(self.table_name, book.model_dump())

    def get_all_books(self):
        data = self.engine.select(self.table_name, "*")
        return [Book.model_validate(d) for d in data]

    def get_book_by_id(self, id: int):
        data = self.engine.select(self.table_name, "*", {"id": id})
        if data:
            return Book.model_validate(data[0])

    def update_book(self, id: int, data: UpdateBook):
        return self.engine.update(
            self.table_name, data.model_dump(exclude_none=True), {"id": id}
        )

    def set_available(self, id: int, val: bool, member_id: int | None):
        self.engine.update(
            self.table_name,
            {"is_available": val, "borrowed_by_member_id": member_id},
            {"id": id},
        )

    def count_total_books(self):
        data = self.engine.count(self.table_name, "*")
        return data[0]['COUNT(*)']

    def count_available_books(self):
        data = self.engine.count(self.table_name, "*", {"is_available":True})
        return data[0]['COUNT(*)']

    def count_borrowed_books(self):
        data = self.engine.count(self.table_name, "*", {"is_available":False})
        return data[0]['COUNT(*)']

    def count_by_genre(self):
        data = self.engine.count(self.table_name, "*", None, "genre", "genre")
        return data

    def count_active_borrows_by_member(self, member_id:int):
        data = self.engine.count(self.table_name, "*", {"borrowed_by_member_id":member_id})
        return data
