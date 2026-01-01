from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()


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


books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": "1925-04-10",
        "page_count": 180,
        "language": "English",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English",
    },
    {
        "id": 3,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton, Whitehall",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English",
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 214,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "publisher": "Harper & Brothers",
        "published_date": "1851-10-18",
        "page_count": 635,
        "language": "English",
    }
]


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_data: UpdateBook) -> dict:
    for book in books:
        if book["id"] == book_id:
            update_data = book_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                book[key] = value
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
