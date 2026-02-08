from typing import Literal
from pydantic import BaseModel, Field, HttpUrl, NonNegativeInt, PositiveInt, StrictBool

from type_definitions.movies_types import Genre
from .general_models import Pagination

class MovieDTO(BaseModel):
    id: NonNegativeInt
    tmdb_id: NonNegativeInt | None = None
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(max_length=5000)
    poster_url: HttpUrl | Literal[""]
    release_year: PositiveInt
    rating: float = Field(ge=0, le=10)
    genres: list[Genre]
    youtube_video_id: str = Field(pattern=r'^([\w-]{11}|)$')

class MovieListPaginated(BaseModel):
    movies: list[MovieDTO]
    pagination: Pagination

class MovieListResponse(BaseModel):
    success: StrictBool
    data: MovieListPaginated