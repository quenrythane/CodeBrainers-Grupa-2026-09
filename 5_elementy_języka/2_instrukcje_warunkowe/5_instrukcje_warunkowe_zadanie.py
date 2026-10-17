

# 1. stwórz 2 zmienne - imie i wiek
# 2. stwórz warunek że jeżeli imię jest męskie i wiek jset >= 18 to wypisz "możesz iść na pobór do wojska"
# 3. jeżeli imię jest żeńskie i wiek jest >= 18 to wypisz "kobieta dorosła"
# 4. jeżeli wiek jest < 18 to wypisz "niepełnoletni"


imie = "Adam"
wiek = 30


"""
if imię_męskie and wiek_18+:
    print("możesz iść na pobór do wojska")
"""


if imie[-1] != "a" and wiek >= 18:  #

    
    print("Możesz iść na pobór do wojska - werjsa 1")
# if True and True:  #
#     print("Możesz iść na pobór do wojska")


# 2. stwórz warunek że jeżeli imię jest męskie i wiek jset >= 18 to wypisz "możesz iść na pobór do wojska"
czy_mężczyzna = imie[-1] != "a"
czy_pełnoletni = wiek >= 18
if czy_mężczyzna and czy_pełnoletni:
    print("możesz iść na pobór do wojska - werjsa 2")

# 3. jeżeli imię jest żeńskie i wiek jest >= 18 to wypisz "kobieta dorosła"
elif not czy_mężczyzna and czy_pełnoletni:
    print("kobieta dorosła")

# 4. jeżeli wiek jest < 18 to wypisz "niepełnoletni"
elif not czy_pełnoletni:
    print("niepełnoletni")

# zabezpiecznie na nieobsłużone warunki
else:
    print("poza zakresem")


