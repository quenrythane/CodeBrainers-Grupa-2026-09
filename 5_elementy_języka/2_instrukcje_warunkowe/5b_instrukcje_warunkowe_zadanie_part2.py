# 1. stwórz 2 zmienne - imie i wiek
# 2. stwórz warunek że jeżeli imię jest męskie i wiek jset >= 18 to wypisz "możesz iść na pobór do wojska"
# 3. jeżeli imię jest żeńskie i wiek jest >= 18 to wypisz "kobieta dorosła"
# 4. jeżeli wiek jest < 18 to wypisz "niepełnoletni"

imie = "Adam"
wiek = 30

czy_mężczyzna = imie[-1] != "a"
czy_pełnoletni = wiek >= 18

# tak nie róbmy - starajmy się nie zagnieżdżać if'ów
if czy_mężczyzna:
    if czy_pełnoletni:
        print("Możesz iść na pobór do wojska - werjsa 1")
    else:
        print("niepełnoletni")
elif not czy_mężczyzna:
    if czy_pełnoletni:
        print("kobieta dorosła")
    else:
        print("niepełnoletni")
else:
    print("poza zakresem")


# to jest rozwiązanie dosłowne z polecnia
if czy_mężczyzna and czy_pełnoletni:
    print("możesz iść na pobór do wojska - werjsa 2")
elif not czy_mężczyzna and czy_pełnoletni:
    print("kobieta dorosła")
elif not czy_pełnolteni:
    print("niepełnoletni")
else:
    print("poza zakresem")


# strategia odsiewania warunków - odsiewamy ludzi którzy nie mogą trafić do wojska
if not czy_pełnolteni:  # odsiewamy dzieci
    print("niepełnoletni")
elif not czy_mężczyzna:  # odsiewamy kobiety
    print("kobieta dorosła")
else:  # zostają sami dorośli mężczyźni
    print("możesz iść na pobór do wojska - werjsa 2")



