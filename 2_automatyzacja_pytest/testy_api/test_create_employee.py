# Testy dla endpointu POST /api/employees (tworzenie nowego pracownika)

import pytest
import requests


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
def test_create_employee_success(base_url, auth_headers, valid_employee_payload):
    # Arrange
    payload = valid_employee_payload.copy()
    payload["name"] = "Piotr Zieliński"
    payload["salary"] = 15000
    payload["age"] = 32
    payload["position"] = "Senior QA"
    payload["on_leave"] = False

    created_id = None
    try:
        # Act
        response = requests.post(f"{base_url}/employees", headers=auth_headers, json=payload)

        # Assert
        assert response.status_code == 200, f"Oczekiwano statusu 200, otrzymano {response.status_code}: {response.text}"
        response_body = response.json()

        assert "id" in response_body and isinstance(response_body["id"], int)
        assert response_body["id"] > 0
        created_id = response_body["id"]

        assert response_body["name"] == payload["name"]
        assert response_body["salary"] == payload["salary"]
        assert response_body["age"] == payload["age"]
        assert response_body["position"] == payload["position"]
        assert response_body["on_leave"] == payload["on_leave"]
    finally:
        # Teardown / Cleanup
        if created_id is not None:
            requests.delete(f"{base_url}/employees/{created_id}", headers=auth_headers)


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
def test_create_employee_unauthorized(base_url, valid_employee_payload):
    # Act - próba utworzenia bez nagłówka Authorization
    response = requests.post(f"{base_url}/employees", json=valid_employee_payload)

    # Assert
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
@pytest.mark.parametrize(
    "invalid_payload, expected_error_type",
    [
        (
            {"name": "", "salary": 5000, "age": 25, "position": "Junior QA"},
            "string_too_short",
        ),
        (
            {"name": "Jan Kowalski", "salary": 0, "age": 25, "position": "Junior QA"},
            "greater_than_equal",
        ),
        (
            {"name": "Jan Kowalski", "salary": 250000, "age": 25, "position": "Junior QA"},
            "less_than_equal",
        ),
        (
            {"name": "Jan Kowalski", "salary": 5000, "age": 17, "position": "Junior QA"},
            "greater_than_equal",
        ),
        (
            {"name": "Jan Kowalski", "salary": 5000, "age": 66, "position": "Junior QA"},
            "less_than_equal",
        ),
        (
            {"name": "Jan Kowalski", "salary": 5000, "age": 25, "position": "Developer"},
            "enum",
        ),
        (
            {"salary": 5000, "age": 25, "position": "Junior QA"},  # brak pola name
            "missing",
        ),
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
def test_create_employee_validation_errors(base_url, auth_headers, invalid_payload, expected_error_type):
    # Act
    response = requests.post(f"{base_url}/employees", headers=auth_headers, json=invalid_payload)

    # Assert
    assert response.status_code == 422, f"Oczekiwano błędu walidacji 422, otrzymano {response.status_code}"
    response_body = response.json()
    assert "detail" in response_body

    error_types = [error.get("type") for error in response_body["detail"]]
    assert expected_error_type in error_types, (
        f"Oczekiwano typu błędu '{expected_error_type}' w {error_types}"
    )
