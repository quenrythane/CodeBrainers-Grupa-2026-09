# 1. Przyjmij od użytkownika dwie liczby, które chciałby ze sobą podzielić.
# 2. Zabezpiecz ten program na wypadek różnych nieprzewidzianych zdarzeń.
    # liczba_2 != 0
    # int(pięć)
    # 5.5 <- n.d.



try:
    liczba_1 = float(input("Podaj pierwszą liczbę: "))
    liczba_2 = float(input("Podaj drugą liczbę: "))
    wynik = liczba_1 / liczba_2
    print(f"Wynik dzielenia to : {wynik}")

except ZeroDivisionError as błąd:
    print(f"Wystąpił błąd dzielenia przez zero : {str(błąd).upper()}")

except TypeError as błąd:
    print(f"Wystąpił błąd : {str(błąd).upper()}")

except Exception as błąd:
    print(f"Wystąpił błąd : {str(błąd).upper()}")




