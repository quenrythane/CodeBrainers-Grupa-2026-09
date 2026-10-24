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

