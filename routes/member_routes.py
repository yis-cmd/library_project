from fastapi import APIRouter

from database.base_models import CreateMember, UpdateMember

member_router = APIRouter()

member_router.post("/")
def create_member(data:CreateMember):
    pass

member_router.get("/")
def get_all_members():
    pass

member_router.get("/{id}")
def get_member_by_id(id:int):
    pass

member_router.put("/{id}")
def update_member(id:int, updates:UpdateMember):
    pass

member_router.put("/{id}/deactivate")
def deactivate_member(id:int):
    pass

member_router.put("/{id}/activate")
def activate_member(id:int):
    pass

