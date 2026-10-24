import pytest

@pytest.fixture
def uzytkownik_premium():
    słownik = {
        "username": "tester_pro",
        "email": "tester@example.com",
        "is_premium": True,
        "punkty": 120
    }
    return słownik


    