from fastapi import FastAPI
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel", rating=5),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel", rating=4),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", description="Classic novel", rating=4),
    Book(id=4, title="The Catcher in the Rye", author="J.D. Salinger", description="Coming-of-age novel", rating=3),
    Book(id=5, title="Brave New World", author="Aldous Huxley", description="Dystopian novel", rating=4),
]

app = FastAPI()

@app.get("/books", response_model=list[Book])
def get_books():
    """
    Get all books.
    """
    return BOOKS

@app.post('/books', response_model=Book)
def create_book(book: Book):
    """
    Create a new book.
    """
    BOOKS.append(book)
    return book
