from pydantic import BaseModel, PositiveInt, StrictBool

class Pagination(BaseModel):
    page: PositiveInt
    limit: PositiveInt
    total: PositiveInt
    totalPages: PositiveInt

class ErrorResponse(BaseModel):
    success: StrictBool
    error: str
    message: str
