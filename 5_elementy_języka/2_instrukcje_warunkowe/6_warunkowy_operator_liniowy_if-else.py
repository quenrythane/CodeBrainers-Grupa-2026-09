imie = "Adam"
czy_mężczyzna = imie[-1] != "a"

if czy_mężczyzna:
    print("Jesteś mężczyzną")
else:
    print("Jesteś kobietą")


# kup_lody_czekoladowe if lody_czekoladowe_dostępne else kup_lody_waniliowe
wynik = print("Jesteś mężczyzną") if czy_mężczyzna else print("Jesteś kobietą")
