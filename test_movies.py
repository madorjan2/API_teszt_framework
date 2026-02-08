import requests
import pytest

baseUrl = "http://localhost:3000/api"

def test_positive_list_all_movies():
    res = requests.get(f"{baseUrl}/movies")
    assert res.status_code == 200
    res_json = res.json()
    assert res_json["success"]
    assert len(res_json["data"]["movies"]) > 0
    for movie in res_json["data"]["movies"]:
        assert "id" in movie
        assert "title" in movie
        assert "release_year" in movie

def test_positive_list_movies_with_limit():
    res = requests.get(f"{baseUrl}/movies?limit=5")
    assert res.status_code == 200
    res_json = res.json()
    assert res_json["success"]
    assert len(res_json["data"]["movies"]) == 5
    for movie in res_json["data"]["movies"]:
        assert "id" in movie
        assert "title" in movie
        assert "release_year" in movie

def test_positive_list_movies_filtering():
    res = requests.get(f"{baseUrl}/movies?year=1994")
    assert res.status_code == 200
    res_json = res.json()
    assert res_json["success"]
    for movie in res_json["data"]["movies"]:
        assert "id" in movie
        assert "title" in movie
        assert "release_year" in movie
        assert movie["release_year"] == 1994

def test_positive_list_movies_sorted():
    res = requests.get(f"{baseUrl}/movies?sort=title")
    assert res.status_code == 200
    res_json = res.json()
    assert res_json["success"]
    movies = res_json["data"]["movies"]
    assert all(movies[i]["title"] <= movies[i + 1]["title"] for i in range(len(movies) - 1))
    for movie in res_json["data"]["movies"]:
        assert "id" in movie
        assert "title" in movie
        assert "release_year" in movie

@pytest.mark.xfail(reason="Bugticket-123", strict=True)
def test_negative_invalid_sort_parameter():
    res = requests.get(f"{baseUrl}/movies?sort=invalid")
    assert res.status_code == 400
    res_json = res.json()
    assert not res_json["success"]
    assert "Invalid sort parameter" in res_json["message"]