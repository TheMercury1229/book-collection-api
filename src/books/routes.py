from fastapi import APIRouter, status
from src.books.book_data import books
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, UpdateBook
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Book])
async def get_all_books():
    return books


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.patch("/{book_id}")
async def update_book(book_id: int, book_data: UpdateBook) -> dict:
    for book in books:
        if book["id"] == book_id:
            update_data = book_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                book[key] = value
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
