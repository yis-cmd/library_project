from fastapi import APIRouter

import library

report_router = APIRouter()

report_router.get("/summary")
def get_over_all_report():
    return library.get_report()

report_router.get("/books-by-genre")
def get_number_of_books_by_genre():
    return library.get_books_by_genre()

report_router.get("/top-member")
def get_member():
    return library.get_most_active_member()


