import requests
from datetime import datetime

from models.auth_models import AuthResponseDTO
from models.general_models import ErrorResponse

from pprint import pprint

baseUrl = "http://localhost:3000/api"

def test_positive_register_user():
    payload = {
        "email": f"madi{int(datetime.now().timestamp())}@example.com",
        "password": "Test1234!",
        "username": "madi"
    }
    res = requests.post(f"{baseUrl}/auth/register", json=payload)
    assert res.status_code == 201
    pprint(res.json())
    res = AuthResponseDTO.model_validate(res.json())
    assert res.success
    assert "User registered successfully" in res.message

def test_positive_login_with_admin():
    payload = {
        "email": "admin@example.com",
        "password": "admin123"
    }
    res = requests.post(f"{baseUrl}/auth/login", json=payload)
    assert res.status_code == 200
    res = AuthResponseDTO.model_validate(res.json())
    assert res.success
    assert not res.data.user.is_banned
    assert "Login successful" in res.message

def test_negative_login_with_wrong_password():
    payload = {
        "email": "admin@example.com",
        "password": "wrongpassword"
    }
    res = requests.post(f"{baseUrl}/auth/login", json=payload)
    assert res.status_code == 401
    res = ErrorResponse.model_validate(res.json())
    assert not res.success
    assert "Unauthorized" in res.error
    assert "Invalid email or password" in res.message