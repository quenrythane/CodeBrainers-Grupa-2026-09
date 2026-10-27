# Testy dla endpointu DELETE /api/employees/{emp_id} (usuwanie pracownika)

import pytest
import requests


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.delete_employee
def test_delete_employee_success(base_url, auth_headers, created_employee):
    # Arrange
    emp_id = created_employee["id"]

    # Act
    response = requests.delete(f"{base_url}/employees/{emp_id}", headers=auth_headers)

    # Assert
    assert response.status_code == 200, f"Oczekiwano statusu 200, otrzymano {response.status_code}: {response.text}"
    assert response.json() == {"status": "deleted"}

    # Weryfikacja: ponowna próba pobrania lub usunięcia powinna zwrócić 404 Not Found
    re_delete_response = requests.delete(f"{base_url}/employees/{emp_id}", headers=auth_headers)
    assert re_delete_response.status_code == 404
    assert re_delete_response.json()["detail"] == "Employee not found"

    # Weryfikacja GET: brak usuniętego rekordu na liście pracowników
    get_response = requests.get(f"{base_url}/employees", headers=auth_headers)
    assert get_response.status_code == 200
    ids_in_list = [emp["id"] for emp in get_response.json()]
    assert emp_id not in ids_in_list, f"Pracownik o id {emp_id} nadal znajduje się na liście po usunięciu"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.delete_employee
def test_delete_employee_not_found(base_url, auth_headers):
    # Arrange
    non_existing_id = 999999

    # Act
    response = requests.delete(f"{base_url}/employees/{non_existing_id}", headers=auth_headers)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.delete_employee
def test_delete_employee_unauthorized(base_url, created_employee):
    # Arrange
    emp_id = created_employee["id"]

    # Act - brak nagłówka Authorization
    response = requests.delete(f"{base_url}/employees/{emp_id}")

    # Assert
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


@pytest.mark.api
@pytest.mark.employees
@pytest.mark.delete_employee
def test_delete_employee_invalid_id_type(base_url, auth_headers):
    # Act - przekazanie niepoprawnego typu parametru ścieżki (string zamiast int)
    response = requests.delete(f"{base_url}/employees/niepoprawne_id", headers=auth_headers)

    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()
