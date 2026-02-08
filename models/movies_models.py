from pydantic import BaseModel
from .general_models import Pagination

class MovieDTO(BaseModel):
    id: int
    tmdb_id: int
    title: str
    description: str
    poster_url: str
    release_year: int
    rating: float
    genres: list[str]
    youtube_video_id: str

class MovieListPaginated(BaseModel):
    movies: list[MovieDTO]
    pagination: Pagination

class MovieListResponse(BaseModel):
    success: bool
    data: MovieListPaginated