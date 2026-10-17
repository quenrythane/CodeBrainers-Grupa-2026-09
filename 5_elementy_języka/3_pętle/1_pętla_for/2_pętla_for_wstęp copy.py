
# lista
# słownik
# krotki
# zbiory
# stringi


liczba_powtórzeń = 5
print(f"To zdanie powiem {liczba_powtórzeń} razy")
for i in range(liczba_powtórzeń):
    print(f"To zdanie powiem mowie po raz {i+1}")
print("\n" + "*" * 50 + "\n")


# [star:end:step]
print(list(range(10)))
print(list(range(10, 15)))
print(list(range(5, 21, 3)))