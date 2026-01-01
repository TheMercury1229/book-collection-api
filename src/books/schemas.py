from pydantic import BaseModel
from typing import List, Optional


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    publisher: Optional[str]
    language: Optional[str]
