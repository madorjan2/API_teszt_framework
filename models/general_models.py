from pydantic import BaseModel

class Pagination(BaseModel):
    page: int
    limit: int
    total: int
    totalPages: int

class ErrorResponse(BaseModel):
    success: bool
    error: str
    message: str
