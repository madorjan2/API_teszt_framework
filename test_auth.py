import requests
from datetime import datetime

baseUrl = "http://localhost:3000/api"

def test_positive_register_user():
    payload = {
        "email": f"madi{int(datetime.now().timestamp())}@example.com",
        "password": "Test1234!",
        "username": "madi"
    }
    res = requests.post(f"{baseUrl}/auth/register", json=payload)
    assert res.status_code == 201
    res_json = res.json()
    assert res_json["success"]
    assert "User registered successfully" in res_json["message"]
    assert "user" in res_json["data"]
    assert res_json["data"]["user"]["email"] == payload["email"]
    assert res_json["data"]["user"]["username"] == payload["username"]
    assert "token" in res_json["data"]

def test_positive_login_with_admin():
    payload = {
        "email": "admin@example.com",
        "password": "admin123"
    }
    res = requests.post(f"{baseUrl}/auth/login", json=payload)
    assert res.status_code == 200
    res_json = res.json()
    assert res_json["success"]
    assert "Login successful" in res_json["message"]
    assert "user" in res_json["data"]
    assert res_json["data"]["user"]["email"] == payload["email"]
    assert "token" in res_json["data"]

def test_negative_login_with_wrong_password():
    payload = {
        "email": "admin@example.com",
        "password": "wrongpassword"
    }
    res = requests.post(f"{baseUrl}/auth/login", json=payload)
    assert res.status_code == 401
    res_json = res.json()
    assert not res_json["success"]
    assert "Invalid email or password" in res_json["message"]