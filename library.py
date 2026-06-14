from database import base_models
from database.book_db import BookDB
from database.member_db import MemberDB

from fastapi import HTTPException

book_manager = BookDB()
member_manager = MemberDB()

def create_book(book:base_models.CreateBook):
    book_manager.create_book(book)
    

def get_all_books():
    return book_manager.get_all_books()
   

def get_book_by_id(id:int):
    data = book_manager.get_book_by_id(id)
    if not data:
        raise HTTPException(404, "book does not exist")
    return data
    

def update_book(id:int, updates:base_models.UpdateBook):
    if not book_manager.get_book_by_id(id):
        raise HTTPException(404, "book does not exist")
    book_manager.update_book(id, updates)
    

def borrow_book(book_id:int, member_id:int):
    book_data = book_manager.get_book_by_id(book_id)
    member_data = member_manager.get_member_by_id(member_id)
    if not book_data or not member_data:
        raise HTTPException(404)
    if not book_data.is_available or not member_data.is_active:
        raise HTTPException(400)
    book_manager.set_available(book_id, False, member_id)
    member_manager.increment_borrows(member_id)

    
def create_member(member:base_models.CreateMember):
    member_manager.create_member(member)

def get_all_members():
    return member_manager.get_all_members()

def get_member_by_id(id):
    data = member_manager.get_member_by_id(id)
    if not data:
        raise HTTPException(404)
    return data

def update_member(id:int, updates:base_models.UpdateMember):
    if not member_manager.get_member_by_id(id):
        raise HTTPException(404)
    member_manager.update_member(id, updates)

def deactivate_member(id:int):
    member_data = member_manager.get_member_by_id(id)
    if not member_data:
        raise HTTPException(404)
    if not member_data.is_active:
        raise HTTPException(400)
    member_manager.deactivate_member(id)

def activate_member(id:int):
    member_data = member_manager.get_member_by_id(id)
    if not member_data:
        raise HTTPException(404)
    if member_data.is_active:
        raise HTTPException(400)
    member_manager.activate_member(id)


def get_report():
    return {
    "total_books": book_manager.count_total_books(),
    "available_books": book_manager.count_available_books(),
    "currently_borrowed": book_manager.count_borrowed_books(),
    "active_members": member_manager.count_active_members()
    }

def get_books_by_genre():
    return book_manager.count_by_genre()

def get_most_active_member():
    return member_manager.get_top_member()