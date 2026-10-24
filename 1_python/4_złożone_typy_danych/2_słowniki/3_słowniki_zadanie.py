słownik_walut = {
    "PLN": "Polski Złoty",
    "EUR": "Euro",
    "USD": "Dolar Amerykański",
    "GBP": "Funt Brytyjski",
    "JPY": "Jen Japoński"
}

# print(słownik_walut["Yuan"])
# print(słownik_walut.get("PLN"))
# waluta = "Yuan"
# print(słownik_walut.get(waluta, f"Nie ma takiej waluty {waluta}"))
# print("nie wyświetlę się jesli był błąd")

# 1. stórz listę wartości słownika
lista_walut = list(słownik_walut.values())
print(lista_walut)

# 2. posotuj listę wartości słownika
lista_walut.sort()
print(lista_walut)



