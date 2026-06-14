from fastapi import FastAPI

from database.base_models import UpdateBook
from routes import book_routes, member_routes, report_routes

app = FastAPI()

app.include_router(book_routes.book_router, prefix="/books")
app.include_router(member_routes.member_router, prefix="/members")
app.include_router(report_routes.report_router, prefix="/reports")
