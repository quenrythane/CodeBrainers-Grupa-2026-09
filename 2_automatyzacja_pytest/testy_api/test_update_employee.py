# Testy dla endpointu PUT /api/employees/{emp_id} (pełna aktualizacja pracownika)

import pytest
import requests


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_success(base_url, auth_headers, created_employee):
    # Arrange
    emp_id = created_employee["id"]
    update_payload = {
        "name": "Marta Lewandowska",
        "salary": 18500,
        "age": 35,
        "position": "QA Lead",
        "on_leave": True,
    }

    # Act
    response = requests.put(f"{base_url}/employees/{emp_id}", headers=auth_headers, json=update_payload)

    # Assert
    assert response.status_code == 200, f"Oczekiwano statusu 200, otrzymano {response.status_code}: {response.text}"
    response_body = response.json()

    assert response_body["id"] == emp_id
    assert response_body["name"] == update_payload["name"]
    assert response_body["salary"] == update_payload["salary"]
    assert response_body["age"] == update_payload["age"]
    assert response_body["position"] == update_payload["position"]
    assert response_body["on_leave"] == update_payload["on_leave"]

    # Weryfikacja GET - sprawdzenie czy zmiana została utrwalona
    get_response = requests.get(f"{base_url}/employees", headers=auth_headers)
    assert get_response.status_code == 200
    employees_list = get_response.json()
    updated_in_list = next((emp for emp in employees_list if emp["id"] == emp_id), None)
    assert updated_in_list is not None, f"Pracownik o id {emp_id} nie został znaleziony na liście"
    assert updated_in_list["name"] == update_payload["name"]
    assert updated_in_list["position"] == update_payload["position"]


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_not_found(base_url, auth_headers, valid_employee_payload):
    # Arrange
    non_existing_id = 999999

    # Act
    response = requests.put(
        f"{base_url}/employees/{non_existing_id}",
        headers=auth_headers,
        json=valid_employee_payload,
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_unauthorized(base_url, created_employee, valid_employee_payload):
    # Arrange
    emp_id = created_employee["id"]

    # Act - brak nagłówka Authorization
    response = requests.put(f"{base_url}/employees/{emp_id}", json=valid_employee_payload)

    # Assert
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.update_employee
def test_update_employee_validation_error(base_url, auth_headers, created_employee):
    # Arrange
    emp_id = created_employee["id"]
    invalid_payload = {
        "name": "Marta Lewandowska",
        "salary": -500,  # niepoprawna pensja (min. 1)
        "age": 15,       # niepoprawny wiek (min. 18)
        "position": "NonExistentRole",
    }

    # Act
    response = requests.put(f"{base_url}/employees/{emp_id}", headers=auth_headers, json=invalid_payload)

    # Assert
    assert response.status_code == 422
    response_body = response.json()
    assert "detail" in response_body
