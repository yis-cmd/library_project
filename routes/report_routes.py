from fastapi import APIRouter

report_router = APIRouter()

report_router.get("/summary")
def get_over_all_report():
    pass

report_router.get("/books-by-genre")
def get_number_of_books_by_genre():
    pass

report_router.get("/top-member")
def get_member():
    pass


