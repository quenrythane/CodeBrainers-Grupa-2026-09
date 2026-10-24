
# stwórz testową która będzie parametryzowana
# funckja ma przyjmować imię i nazwisko i zwracać łączne powitanie np.
# "Witaj, Jan Kowalski" z uwzględniem że pełne imię ma być zwracane zawe z dużej litery
# "imie".capitalize()

# dane testowe
[
    ("Jan", "kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski"),
    ("Jan", "Kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski"),
]


import pytest

def powitanie(imie: str, nazwisko: str):
    powitanie = f"Witaj, {imie.capitalize()} {nazwisko.capitalize()}"
    return powitanie


@pytest.mark.powitanie
@pytest.mark.parametrize("imie, nazwisko, spodziewany_rezultat", [
    ("Jan", "kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski"),
    ("Jan", "Kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski")
])
def test_powitanie(imie, nazwisko, spodziewany_rezultat):
    assert powitanie(imie, nazwisko) == spodziewany_rezultat
