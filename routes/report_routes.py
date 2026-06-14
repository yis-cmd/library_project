from fastapi import APIRouter

from create_logger import create_logger
import library

report_router = APIRouter()
logger = create_logger(__name__)

@report_router.get("/summary")
def get_over_all_report():
    logger.info("GET /reports/summary")
    return library.get_report()

@report_router.get("/books-by-genre")
def get_number_of_books_by_genre():
    logger.info("GET /reports/book-by-genre")
    return library.get_books_by_genre()

@report_router.get("/top-member")
def get_member():
    logger.info("GET /reports/top-member")
    return library.get_most_active_member()


