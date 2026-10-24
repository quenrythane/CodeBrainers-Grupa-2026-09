from kalkulator import dodaj


# Pamiętajmy, żeby w terminalu używać venva
#    Windows Aktywacja venv (Terminal cmd): .\.venv\Scripts\activate.bat
#    Windows Aktywacja venv (PowerShell):  .\.venv\Scripts\Activate.ps1
#    MacOS/Linux Aktywacja venv: source .venv/bin/activate

# Test uruchamiamy poprzez pytest -v

# Test musi zaczynać się od słowa test_
def test_dodaj():
    assert dodaj(1, 1) == 2
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0
    assert dodaj(0, 0) == 0
    assert dodaj(-5, -5) == -10


