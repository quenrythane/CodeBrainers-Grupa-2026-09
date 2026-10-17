"""
1. Listy imion - stwórz listę z 3-ema imionamia
2. dodaj pojedyncze imie do listy
3. stwórz nową listę z 2-ma imiobani i dodaj je do pierwotnej listy
4. stwórz nową listę z 2-ma imiobani i dodaj je na początek listy
5. posortuj tę listę
6. zwróć 4 elementy listy
"""

# 1. Listy imion - stwórz listę z 3-ema imionamia
imiona = ["Ania", "Kasia", "Basia"]

# 2. dodaj pojedyncze imie do listy
imiona.append("Bartek")
print("2:", imiona, "\n")

# 3. stwórz nową listę z 2-ma imiobani i dodaj je do pierwotnej listy
nowe_imiona = ["Krzyś", "Ryś"]
imiona.extend(nowe_imiona)
print("3a:", imiona, "\n")

# imiona.append(nowe_imiona)  # tek nie robimy bo zwróci 3b: ['Ania', 'Kasia', 'Basia', 'Bartek', 'Krzyś', 'Ryś', 👉 ['Krzyś', 'Ryś'] 👈]
# print("3:", imiona, "\n")

# 4. stwórz nową listę z 2-ma imiobani i dodaj je na początek listy
nowe_imiona_2 = ["Celina", "Malina"]
# imiona.insert(0, nowe_imiona_2)
imiona = nowe_imiona_2 + imiona
print("4:", imiona, "\n")

# 5. posortuj tę listę
imiona = sorted(imiona)  # można też odwrotną kolejność reverse=True
print("5:", imiona, "\n")

# 6. zwróć 4 elementy listy
print("6:", imiona[:4], "\n")

# 6*.
print("6*:", imiona[::2], "\n")
print("7*:", imiona[:len(imiona)//2], "\n")



