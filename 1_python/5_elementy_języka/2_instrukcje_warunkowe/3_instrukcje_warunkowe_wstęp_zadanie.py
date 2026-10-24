
imie = "Artur"

# "a"
imie[-1] == "a"  # sprawdzenie czy imie jest żeńskie

# stwórz zmienną imię, która przyjmie imię od użytkownika (input())
# użyj instrukcji warunkowej, jeśli imię jest żeńskie to napisz (print()) RÓŻOWY
# a jeśli imię jest mętskie napisz NIEBIESKI


imie = input("Podaj swoje imię: ")

if imie[-1].lower() == 'a':
    print("RÓŻOWY")

print("koniec programu")

