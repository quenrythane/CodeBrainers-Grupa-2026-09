# i/o - input/ouput
# input - Dane, które wprowadza człowiek.
# output - Dane, które wyświetla/zwraca maszyna.

# imie = input("Podaj Imię: ")
# print(f"Cześć miło mi Cię poznąć {imie}")

# wiek = input("podaj swój wiek: ")
# print(f"Cześć masz {wiek} lat")


"""
Zapytaj użytkownika o imię i wiek,
Powiedz mu "Cześć imię, za 5 lat będziesz miał <wiek+5> lat.
"""

imie = input("Podaj imie: ")
wiek = int(input("Podaj wiek: "))
print(f"Cześć {imie}, za 5 lat będziesz miał {wiek+5} lat")
