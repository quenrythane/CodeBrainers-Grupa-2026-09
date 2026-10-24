def dodawanie(liczba_1, liczba_2):
    wynik = liczba_1 + liczba_2
    return wynik
    print("jestem printem")

xd = dodawanie(4, 5)
print(xd)


def dzielenie(liczba_1: int, liczba_2: int = 2) -> float:
    """
    Jestem komentarzem który ma podpowiedzieć jak funkcja działa.\n
    Dziele liczbą 1 przez liczbe 2 i zwracam wynik float\n
    """
    if liczba_2 == 0:
        return "Nie można dzielić przez zero"
    return liczba_1 / liczba_2


print(dzielenie("5", "10"))
print(dzielenie(10))

