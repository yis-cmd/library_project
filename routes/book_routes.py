from fastapi import APIRouter

from database.base_models import CreateBook, UpdateBook
import library

book_router = APIRouter()

book_router.post("/")
def create_book(data:CreateBook):
    library.create_book(data)

book_router.get("/")
def get_all_books():
    return library.get_all_books()

book_router.get("/{id}")
def get_book_by_id(id:int):
    return library.get_book_by_id(id)

book_router.put("/{id}")
def update_book(id:int, updates:UpdateBook):
    library.update_book(id, updates)

book_router.put("/{id}/borrow/{member_id}")
def borrow_book(id:int, member_id:int):
    library.borrow_book(id, member_id)

book_router.put("/{id}/return/{member_id}")
def return_book(id:int, member_id:int):
    library.return_book(id, member_id)