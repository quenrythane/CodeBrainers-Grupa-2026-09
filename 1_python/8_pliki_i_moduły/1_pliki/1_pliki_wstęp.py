nazwa_pliku = "co_to_jest_python.txt"
poziom_uprawnień = "r"  # "a",  "w"

file = open(nazwa_pliku, poziom_uprawnień, encoding="utf8")

# pełen_tekst = file.read()
# print("pełen_tekst", pełen_tekst, "\n")

# pierwsza_linia = file.readline()  # <- czyta tylko nieprzeczytane linie
# print("pierwsza_linia: ", pierwsza_linia, "\n")

# druga_linia = file.readline()
# print("druga_linia: ", druga_linia, "\n")

pozostałe_linie = file.readlines()  # <- czyta tylko nieprzeczytane linie i zwraca jako lista
# print("pozostałe_linie: ", pozostałe_linie, "\n")

print(len(pozostałe_linie))
for linia in pozostałe_linie:
    print(linia, "\n")


file.close()
