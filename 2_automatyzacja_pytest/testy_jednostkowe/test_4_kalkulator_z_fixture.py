import pytest
from kalkulator import dodaj, podziel



@pytest.mark.dodaj_z_fixture
def test_dodaj(przygotowanie, oczekiwany_wynik_dodawania):
    assert dodaj(1, 2) == oczekiwany_wynik_dodawania

