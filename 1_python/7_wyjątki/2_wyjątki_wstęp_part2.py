
liczba = 5
słowo = input("Podaj mi liczbę do podzielenia: ")

try:
    print("\nChcę spróbować wykonać ten ryzykowny kod\n")
    wynik = liczba / słowo
    print(wynik)
    print("Udało się wykonać ryzykowny kod\n")

except ZeroDivisionError as błąd:
    print(f"Wystąpił błąd Dzielenia przez zero: {str(błąd).upper()}\n")

except TypeError as błąd:
    print(f"Wystąpił błąd Typów: {str(błąd).upper()}\n")

except Exception as błąd:
    print(f"Wystąpił nieznany błąd: {str(błąd).upper()}\n")


print("Chciałbym żeby to się wyświetliło zawsze\n".upper())
