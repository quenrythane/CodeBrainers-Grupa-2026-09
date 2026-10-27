# Testy dla endpointu POST /api/employees (tworzenie nowego pracownika)

import pytest
import requests


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
def test_create_employee_success(base_url, auth_headers, new_employee_payload):
    created_id = None
    try:
        # Act
        response = requests.post(f"{base_url}/employees", headers=auth_headers, json=new_employee_payload)

        # Assert
        assert response.status_code == 200, f"Oczekiwano statusu 200, otrzymano {response.status_code}: {response.text}"
        response_body = response.json()

        assert "id" in response_body and isinstance(response_body["id"], int)
        assert response_body["id"] > 0
        created_id = response_body["id"]

        assert response_body["name"] == new_employee_payload["name"]
        assert response_body["salary"] == new_employee_payload["salary"]
        assert response_body["age"] == new_employee_payload["age"]
        assert response_body["position"] == new_employee_payload["position"]
        assert response_body["on_leave"] == new_employee_payload["on_leave"]
    finally:
        # Teardown / Cleanup
        if created_id is not None:
            requests.delete(f"{base_url}/employees/{created_id}", headers=auth_headers)


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
def test_create_employee_unauthorized(base_url, new_employee_payload, unauthorized_response):
    # Act - próba utworzenia bez nagłówka Authorization
    response = requests.post(f"{base_url}/employees", json=new_employee_payload)

    # Assert
    assert response.status_code == 401
    assert response.json() == unauthorized_response


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.create_employee
def test_create_employee_validation_errors(base_url, auth_headers, invalid_employee_data):
    # Arrange
    invalid_payload, expected_error_type = invalid_employee_data

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
