import pytest
import requests

@pytest.mark.api
@pytest.mark.api_login
def test_login(base_url, login_data, correct_login_payload, correct_login_response):
    # Act
    response = requests.post(f"{base_url}/login", json=correct_login_payload)

    # Assert
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["access_token"]
    assert len(response_body["access_token"]) >= correct_login_response["access_token_len"]
    assert response_body["token_type"] == correct_login_response["token_type"]
    assert response_body["expires_in"] == correct_login_response["expires_in"]
