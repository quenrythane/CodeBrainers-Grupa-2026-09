słownik_walut = {
    "PLN": "Polski Złoty",
    "EUR": "Euro",
    "USD": "Dolar Amerykański",
    "GBP": "Funt Brytyjski",
    "JPY": "Jen Japoński",
    "PLN": "xd",  # klucze mogą się powtarzać - słownik nadpisze stare wartości nowymi
}

print(słownik_walut.get("PLN"))

słownik_walut["PLN"] = "Nowy Polski Złoty"  # możemy nadpisywać wartości pod kluczem
print(słownik_walut.get("PLN"))



