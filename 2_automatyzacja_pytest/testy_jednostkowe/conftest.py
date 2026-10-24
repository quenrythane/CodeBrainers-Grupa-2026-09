import pytest

@pytest.fixture()
def przygotowanie():
    print("\nWłaśnie rozpoczynam test xd xd".upper())
    print("Wykona PRZED testem\n")

    yield

    print("\nWykona PO teście")


# def przygotowanie_autouse(scope="function"):
@pytest.fixture(scope="session", autouse=True)
def przygotowanie_autouse():
    print("\nTo się dzieje na POCZĄTKU sesji testowej")
    yield
    print("\nTo się dzieje na KOŃCU sesji testowej")


@pytest.fixture
def oczekiwany_wynik_dodawania():
    return 3
    {
        "name": "Artur",
        "salary": 10000

    }