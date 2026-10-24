import pytest
from kalkulator import dodaj, podziel


# Pamiętajmy, żeby w terminalu używać venva
#    Windows Aktywacja venv (Terminal cmd): .\.venv\Scripts\activate.bat
#    Windows Aktywacja venv (PowerShell):  .\.venv\Scripts\Activate.ps1
#    MacOS/Linux Aktywacja venv: source .venv/bin/activate

# Test uruchamiamy poprzez wpisanie w terminalu z aktywowanym venv:
# pytest -v

# Test musi zaczynać się od słowa test_

@pytest.mark.dodaj
def test_dodaj():
    # assert dodaj(1, 1) == 2
    # assert dodaj(2, 3) == 5
    # assert dodaj(-1, 1) == 0
    # assert dodaj(0, 0) == 0
    # assert dodaj(-5, -5) == -10


    for num_1, num_2, expected_result in [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 5),
        (0, 0, 0),
        (-5, -5, -10)
    ]:
        assert dodaj(num_1, num_2) == expected_result

