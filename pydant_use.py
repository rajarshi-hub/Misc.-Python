from pydantic import BaseModel, field_validator, ValidationInfo


class LibraryBook(BaseModel):

    book_name: str
    pages: int
    author: str
    like_percentage: int

    @field_validator('like_percentage')
    def validate_like_percentage(cls, value: int):
        if 0 <= value <= 100:
            return True
        raise ValueError('Percentage should be between 0 and 100')


book = LibraryBook(
    book_name='Tale of two Cities', pages=67, author='John Dickens', like_percentage=89
)