# Testy dla endpointu PUT /api/employees/{emp_id} (pełna aktualizacja pracownika)

import pytest
import requests


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_success(base_url, auth_headers, created_employee, update_employee_payload):
    # Arrange
    emp_id = created_employee["id"]

    # Act
    response = requests.put(f"{base_url}/employees/{emp_id}", headers=auth_headers, json=update_employee_payload)

    # Assert
    assert response.status_code == 200, f"Oczekiwano statusu 200, otrzymano {response.status_code}: {response.text}"
    response_body = response.json()

    assert response_body["id"] == emp_id
    assert response_body["name"] == update_employee_payload["name"]
    assert response_body["salary"] == update_employee_payload["salary"]
    assert response_body["age"] == update_employee_payload["age"]
    assert response_body["position"] == update_employee_payload["position"]
    assert response_body["on_leave"] == update_employee_payload["on_leave"]

    # Weryfikacja GET - sprawdzenie czy zmiana została utrwalona
    get_response = requests.get(f"{base_url}/employees", headers=auth_headers)
    assert get_response.status_code == 200
    employees_list = get_response.json()
    updated_in_list = next((emp for emp in employees_list if emp["id"] == emp_id), None)
    assert updated_in_list is not None, f"Pracownik o id {emp_id} nie został znaleziony na liście"
    assert updated_in_list["name"] == update_employee_payload["name"]
    assert updated_in_list["position"] == update_employee_payload["position"]


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_not_found(
    base_url, auth_headers, non_existing_employee_id, update_employee_payload, employee_not_found_response
):
    # Act
    response = requests.put(
        f"{base_url}/employees/{non_existing_employee_id}",
        headers=auth_headers,
        json=update_employee_payload,
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == employee_not_found_response


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_unauthorized(
    base_url, created_employee, update_employee_payload, unauthorized_response
):
    # Arrange
    emp_id = created_employee["id"]

    # Act - brak nagłówka Authorization
    response = requests.put(f"{base_url}/employees/{emp_id}", json=update_employee_payload)

    # Assert
    assert response.status_code == 401
    assert response.json() == unauthorized_response


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_validation_error(
    base_url, auth_headers, created_employee, invalid_update_employee_payload
):
    # Arrange
    emp_id = created_employee["id"]

    # Act
    response = requests.put(f"{base_url}/employees/{emp_id}", headers=auth_headers, json=invalid_update_employee_payload)

    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()
