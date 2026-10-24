import pytest
from kalkulator import dodaj, podziel

@pytest.mark.dodaj_z_parametrami
@pytest.mark.parametrize("num_1, num_2, expected_result", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -5, -10),
    (5, 7, 12)
])
def test_dodaj_z_parametrami(num_1, num_2, expected_result):
    assert dodaj(num_1, num_2) == expected_result


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
