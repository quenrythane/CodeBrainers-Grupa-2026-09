nazwa_pliku = "dane_testowe_2.txt"  # <- jeśli dany plik nie istnieje, to python go stworzy
poziom_uprawnień = "a"  # "r", "a",  "w"
# r - tylko czyta plik
# a - dopisuje nowe rzeczy do istniejącej zawartości pliku
# w - nadpisuje plik nową zawartością, czyści plik jeśli coś w nim było i zapisuje nową treść!

file = open(nazwa_pliku, poziom_uprawnień, encoding="utf8")
file.write("\nHello World!")
# print(file.read())  # <- to zwróci błąd, bo uprawnienie "a" pozwala jedynie pisać po pliku


