from fastapi import FastAPI
from src.books.routes import router as books_router
version = "1.0.0"
app = FastAPI(title="Book Management API", version=version)

app.include_router(books_router, prefix="/api/books", tags=["books"])
