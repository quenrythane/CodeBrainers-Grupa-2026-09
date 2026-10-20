# poprośmy użytkownika o podanie dwóch liczb które będziemy chcieli przez siebie podzielić bez błędu
# prośmy użytkownika tak długo, aż poda poprawne wartości
# Jeśli poda błędne wartości, to powiedzmy mu, co robi źle, żeby był w stanie się skorygować.


while True:
    try:
        input_1 = input("Podaj pierwszą liczbę: ")
        liczba_1 = float(input_1)
        break

    except ValueError:
        print(f"Wpisz liczbę typu 1, 2, etc. Została wpisana błędna wartość: {input_1}")

    except Exception:
        print(f"Niespodziewany błąd. Spróbuj raz jeszcze za chwilę")


while True:
    try:
        input_2 = input("Podaj drugą liczbę: ")
        liczba_2 = float(input_2)
        if liczba_2 == 0.0:
            raise ZeroDivisionError
        break

    except ZeroDivisionError:
        print(f"Podana liczba nie może być = 0")

    except ValueError:
        print(f"Wpisz liczbę typu 1, 2, etc. Została wpisana błędna wartość: {input_2}")

    except Exception:
        print(f"Niespodziewany błąd. Spróbuj raz jeszcze za chwilę")

wynik = liczba_1 / liczba_2
print(f"Wynik dzielenia to : {wynik}")


