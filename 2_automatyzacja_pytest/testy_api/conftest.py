import logging
import pytest
import requests


@pytest.fixture(autouse=True)
def logger(request):
    log = logging.getLogger("tests")
    log.info("START: %s", request.node.nodeid)
    yield log
    log.info("KONIEC: %s", request.node.nodeid)



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


# ==============================================================================
# Employee Test Data Fixtures (Payloads)
# ==============================================================================

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
def new_employee_payload():
    return {
        "name": "Piotr Zieliński",
        "salary": 15000,
        "age": 32,
        "position": "Senior QA",
        "on_leave": False
    }


@pytest.fixture()
def update_employee_payload():
    return {
        "name": "Marta Lewandowska",
        "salary": 18500,
        "age": 35,
        "position": "QA Lead",
        "on_leave": True
    }


@pytest.fixture()
def invalid_update_employee_payload():
    return {
        "name": "Marta Lewandowska",
        "salary": -500,
        "age": 15,
        "position": "NonExistentRole",
        "on_leave": True
    }


@pytest.fixture(
    params=[
        ({"name": "", "salary": 5000, "age": 25, "position": "Junior QA"}, "string_too_short"),
        ({"name": "Jan Kowalski", "salary": 0, "age": 25, "position": "Junior QA"}, "greater_than_equal"),
        ({"name": "Jan Kowalski", "salary": 250000, "age": 25, "position": "Junior QA"}, "less_than_equal"),
        ({"name": "Jan Kowalski", "salary": 5000, "age": 17, "position": "Junior QA"}, "greater_than_equal"),
        ({"name": "Jan Kowalski", "salary": 5000, "age": 66, "position": "Junior QA"}, "less_than_equal"),
        ({"name": "Jan Kowalski", "salary": 5000, "age": 25, "position": "Developer"}, "enum"),
        ({"salary": 5000, "age": 25, "position": "Junior QA"}, "missing"),
    ],
    ids=[
        "empty_name",
        "salary_below_minimum",
        "salary_above_maximum",
        "age_below_minimum",
        "age_above_maximum",
        "invalid_position_enum",
        "missing_required_name",
    ],
)
def invalid_employee_data(request):
    return request.param


# ==============================================================================
# Employee Identifiers and Expected Responses Fixtures
# ==============================================================================

@pytest.fixture()
def non_existing_employee_id():
    return 999999


@pytest.fixture()
def invalid_employee_id():
    return "niepoprawne_id"


@pytest.fixture()
def delete_success_response():
    return {"status": "deleted"}


@pytest.fixture()
def employee_not_found_response():
    return {"detail": "Employee not found"}


@pytest.fixture()
def unauthorized_response():
    return {"detail": "Not authenticated"}


# ==============================================================================
# Employee State Management Fixtures (Setup & Teardown)
# ==============================================================================

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