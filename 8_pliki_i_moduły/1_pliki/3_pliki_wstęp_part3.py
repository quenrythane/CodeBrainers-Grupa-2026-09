nazwa_pliku = "dane_testowe.txt"


with open(nazwa_pliku, "r", encoding="utf8") as plik:
    for _ in range(3):
        print(plik.readline().upper())
    # print(plik.readline().upper())
    # print(plik.readline().upper())

# print(plik.readline().upper())  # <- poza zagnieżdżeniem nie można plik już jest niedostępny


