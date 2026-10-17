słownik_owoców = {
    "jabłko": "czerwone",
    "banan": "żółty",
    "winogrono": "fioletowe",
    "gruszka": "zielona"
}


for klucz, wartość in słownik_owoców.items():  # pamiętać o użyciu metody items()
    print(f"Pod kluczem {klucz.upper()} znajduej się wartość {wartość.upper()}")

print()

for element in słownik_owoców:
    print(element)