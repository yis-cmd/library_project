from enum import StrEnum

from pydantic import BaseModel, Field, EmailStr


class Genre(StrEnum):
    Fiction: str
    Non_Fiction: str
    Science: str
    History: str
    Other: str


class Book(BaseModel):
    id: int
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    genre: Genre
    is_available: bool
    borrowed_by_member_id: int | None


class CreateBook(BaseModel):
    title: str
    author: str
    genre: Genre

class InsertBook(BaseModel):
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    genre: Genre
    is_available: bool = True
    borrowed_by_member_id: int | None
class Member(BaseModel):
    id: int
    name: str = Field(max_length=50)
    email: EmailStr
    is_active: bool
    total_borrows: int


class CreateMember(BaseModel):
    name: str
    email: EmailStr
