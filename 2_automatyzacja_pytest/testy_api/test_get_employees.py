# stwórz test dla EP GET /api/employees

import pytest
import requests

@pytest.mark.api
@pytest.mark.employees
@pytest.mark.get_employees
def test_get_employees(base_url, auth_headers):
    # Act
    response = requests.get(f"{base_url}/employees", headers=auth_headers)

    # Assert
    response_body = response.json()
    print(response_body)
    assert True