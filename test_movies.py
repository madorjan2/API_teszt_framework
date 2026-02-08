import requests
import pytest

from models.movies_models import MovieListResponse
from models.general_models import ErrorResponse

baseUrl = "http://localhost:3000/api"

def test_positive_list_all_movies():
    res = requests.get(f"{baseUrl}/movies")
    assert res.status_code == 200
    res = MovieListResponse.model_validate(res.json())
    assert res.success
    assert len(res.data.movies) > 0
    

def test_positive_list_movies_with_limit():
    res = requests.get(f"{baseUrl}/movies?limit=5")
    assert res.status_code == 200
    res = MovieListResponse.model_validate(res.json())
    assert res.success
    assert len(res.data.movies) == 5
    

def test_positive_list_movies_filtering():
    res = requests.get(f"{baseUrl}/movies?year=1994")
    assert res.status_code == 200
    res = MovieListResponse.model_validate(res.json())
    assert res.success
    for movie in res.data.movies:
        assert movie.release_year == 1994

def test_positive_list_movies_sorted():
    res = requests.get(f"{baseUrl}/movies?sort=title")
    assert res.status_code == 200
    res = MovieListResponse.model_validate(res.json())
    assert res.success
    titles = [movie.title for movie in res.data.movies]
    assert titles == sorted(titles)

@pytest.mark.xfail(reason="Bugticket-123", strict=True)
def test_negative_invalid_sort_parameter():
    res = requests.get(f"{baseUrl}/movies?sort=invalid")
    assert res.status_code == 400
    res = ErrorResponse.model_validate(res.json())
    assert not res.success
    assert "ValidationError" in res.error
    assert "Invalid sort parameter" in res.message