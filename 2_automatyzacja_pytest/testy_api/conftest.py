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


@pytest.fixture()
def valid_employee_payload():
    return {
        "name": "Jan Kowalski",
        "salary": 12000,
        "age": 30,
        "position": "Mid QA",
        "on_leave": False
    }


@pytest.fixture()
def created_employee(base_url, auth_headers, valid_employee_payload):
    # Setup: Utworzenie pracownika przed testem
    response = requests.post(f"{base_url}/employees", headers=auth_headers, json=valid_employee_payload)
    assert response.status_code == 200, f"Setup nie powiódł się: {response.text}"
    employee = response.json()
    yield employee

    # Teardown: Próba usunięcia pracownika po teście (jeśli nadal istnieje)
    requests.delete(f"{base_url}/employees/{employee['id']}", headers=auth_headers)


@pytest.fixture()
def reset_employees(base_url, auth_headers):
    # Przywrócenie stanu początkowego bazy pracowników
    response = requests.post(f"{base_url}/employees/reset", headers=auth_headers)
    assert response.status_code == 200
    return response.json()