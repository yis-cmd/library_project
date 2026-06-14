from fastapi import APIRouter

from create_logger import create_logger
from database.base_models import CreateMember, UpdateMember
import library

member_router = APIRouter()
logger = create_logger(__name__)

@member_router.post("/")
def create_member(data:CreateMember):
    logger.info("POST /members/")
    library.create_member(data)

@member_router.get("/")
def get_all_members():
    logger.info("GET /members/")
    return library.get_all_members()

@member_router.get("/{id}")
def get_member_by_id(id:int):
    logger.info(f"GET /members/{id}")
    return library.get_member_by_id(id)

@member_router.put("/{id}")
def update_member(id:int, updates:UpdateMember):
    logger.info(f"PUT /members/{id}")
    library.update_member(id, updates)

@member_router.put("/{id}/deactivate")
def deactivate_member(id:int):
    logger.info(f"PUT /members/{id}/deactivate")
    library.deactivate_member(id)

@member_router.put("/{id}/activate")
def activate_member(id:int):
    logger.info(f"PUT /members/{id}/activate")
    library.activate_member(id)

