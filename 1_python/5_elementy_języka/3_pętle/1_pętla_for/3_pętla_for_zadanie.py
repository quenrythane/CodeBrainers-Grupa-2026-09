# dla listy imion przywitaj się z każdą osobą w nastepujący spsosób
# Jeśli jest to mężczyzna, powiedz: „Dzień dobry, panie [imię]”.
# Jeśli jest to kobieta, powiedz: „Dzień dobry, pani [imię]”.


imiona = ["Artur", "Basia", "Celina", "Dawid", "Eliza"]


imiona = ["Artur", "Basia", "Celina", "Dawid", "Eliza"]

for imie in imiona:
    czy_kobieta = imie[-1] == "a"
    if czy_kobieta:
        print(f"Dzien dobry Pani {imie}")
    else:
        print(f"Dzien dobry Panie {imie}")


