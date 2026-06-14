from fastapi import APIRouter

from database.base_models import CreateMember, UpdateMember
import library

member_router = APIRouter()

member_router.post("/")
def create_member(data:CreateMember):
    library.create_member(data)

member_router.get("/")
def get_all_members():
    return library.get_all_members()

member_router.get("/{id}")
def get_member_by_id(id:int):
    return library.get_member_by_id(id)

member_router.put("/{id}")
def update_member(id:int, updates:UpdateMember):
    library.update_member(id, updates)

member_router.put("/{id}/deactivate")
def deactivate_member(id:int):
    library.deactivate_member(id)

member_router.put("/{id}/activate")
def activate_member(id:int):
    library.activate_member(id)

