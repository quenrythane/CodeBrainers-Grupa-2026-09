słownik_owoców = {
    "jabłko": "czerwone",
    "banan": "żółty",
    "winogrono": "fioletowe",
    "gruszka": "zielona"
}

# lista kluczy
print(słownik_owoców.keys())
print(type(słownik_owoców.keys()), "\n")

lista_kluczy = list(słownik_owoców.keys())
print(lista_kluczy)
print(type(lista_kluczy), "\n")

# lista wartości
lista_wartości = list(słownik_owoców.values())
print(lista_wartości)
print(type(lista_wartości), "\n")

# lista itemów
lista_itemów = list(słownik_owoców.items())  # [("jabłko", "czerwone"), ]
print(lista_itemów)
print(type(lista_itemów), "\n")



