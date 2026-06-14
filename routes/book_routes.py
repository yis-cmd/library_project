from fastapi import APIRouter

from create_logger import create_logger
from database.base_models import CreateBook, UpdateBook
import library

book_router = APIRouter()
logger = create_logger(__name__)

@book_router.post("/")
def create_book(data:CreateBook):
    logger.info(f"POST /books/")
    library.create_book(data)

@book_router.get("/")
def get_all_books():
    logger.info(f"GET /books/")
    return library.get_all_books()

@book_router.get("/{id}")
def get_book_by_id(id:int):
    logger.info(f"GET /books/{id}")
    return library.get_book_by_id(id)

@book_router.put("/{id}")
def update_book(id:int, updates:UpdateBook):
    logger.info(f"PUT /books/{id}")
    library.update_book(id, updates)

@book_router.put("/{id}/borrow/{member_id}")
def borrow_book(id:int, member_id:int):
    logger.info(f"PUT /books/{id}/borrow/{member_id}")
    library.borrow_book(id, member_id)

@book_router.put("/{id}/return/{member_id}")
def return_book(id:int, member_id:int):
    logger.info(f"PUT /books/{id}/return/{member_id}")
    library.return_book(id, member_id)