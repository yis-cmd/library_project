from fastapi import APIRouter

from database.base_models import CreateBook, UpdateBook

book_router = APIRouter()

book_router.post("/")
def create_book(data:CreateBook):
    pass

book_router.get("/")
def get_all_books():
    pass

book_router.get("/{id}")
def get_book_by_id(id:int):
    pass

book_router.put("/{id}")
def update_book(id:int, updates:UpdateBook):
    pass

book_router.put("/{id}/borrow/{member_id}")
def borrow_book(id:int, member_id:int):
    pass

book_router.put("/{id}/return/{member_id}")
def return_book(id:int, member_id:int):
    pass
