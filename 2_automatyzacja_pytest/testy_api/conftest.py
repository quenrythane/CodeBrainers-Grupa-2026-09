import pytest
import requests

@pytest.fixture()
def base_url():
    return "http://localhost:8000/api"


@pytest.fixture()
def login_data():
    return {
        "username": "admin",
        "password": "admin"
    }


@pytest.fixture()
def headers():
    return {}


@pytest.fixture()
def auth_headers(base_url, correct_login_payload):
    response = requests.post(f"{base_url}/login", json=correct_login_payload)
    token = response.json()["access_token"]
    return {
        "Authorization": f"Bearer {token}"
    }


@pytest.fixture()
def correct_login_payload(login_data):
    return {
        "username": login_data["username"],
        "password": login_data["password"]
    }

@pytest.fixture()
def correct_login_response(login_data):
    return {
        "access_token_len": 40,
        "token_type": "bearer",
        "expires_in": 600
    }