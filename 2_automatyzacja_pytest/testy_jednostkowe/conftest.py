import pytest
import logging


@pytest.fixture(autouse=True)
def logger(request):
    log = logging.getLogger("tests")
    log.info("START: %s", request.node.nodeid)
    yield log
    log.info("KONIEC: %s", request.node.nodeid)


@pytest.fixture()
def przygotowanie():
    print("\nWłaśnie rozpoczynam test xd xd".upper())
    print("Wykona PRZED testem\n")

    yield

    print("\nWykona PO teście")


# def przygotowanie_autouse(scope="function"):
@pytest.fixture(scope="session", autouse=False)
def przygotowanie_autouse():
    print("\nTo się dzieje na POCZĄTKU sesji testowej")
    yield
    print("\nTo się dzieje na KOŃCU sesji testowej")


@pytest.fixture
def oczekiwany_wynik_dodawania():
    return 3


@pytest.fixture
def uzytkownik_premium():
    # fixture dla zadania 5
    słownik = {
        "username": "tester_pro",
        "email": "tester@example.com",
        "is_premium": True,
        "punkty": 120
    }
    return słownik


