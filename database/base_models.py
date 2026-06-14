from enum import StrEnum

from pydantic import BaseModel, Field, EmailStr


class Genre(StrEnum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    OTHER = "Other"


class Book(BaseModel):
    id: int
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    genre: Genre
    is_available: bool
    borrowed_by_member_id: int | None


class CreateBook(BaseModel):
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    genre: Genre


class InsertBook(CreateBook):
    is_available: bool = True
    borrowed_by_member_id: int | None = None


class UpdateBook(BaseModel):
    title: str | None = Field(max_length=50, default=None)
    author: str | None = Field(max_length=50, default=None)
    genre: Genre | None = None
    is_available: bool | None = None
    borrowed_by_member_id: int | None = None


class Member(BaseModel):
    id: int
    name: str = Field(max_length=50)
    email: EmailStr
    is_active: bool
    total_borrows: int


class CreateMember(BaseModel):
    name: str
    email: EmailStr
