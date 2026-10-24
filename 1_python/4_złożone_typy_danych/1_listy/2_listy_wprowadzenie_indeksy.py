imiona = ["Artur", "Bartek", "Czarek", "Darek", "Ela"]

print(imiona[1])  # "Bartek"
print(imiona[1][-3])  # "t"

print(imiona[::2])

nowa_lista = imiona + imiona[::-1]
print(nowa_lista)

imiona[-1] = "Edward"
print(imiona)

# metody - funkcje wykonywane na obiekcie

# append(20)
lista_xd = []
lista_xd.append(20)  # dodaje pojedynczą rzecz
print("*" * 100)
print("Dodanie elementu 20:", lista_xd)

lista_xd.extend([1, 2, 3])  # rozszerza o nową listę o 3 elementy 1, 2, 3
print("Dodanie extend:", lista_xd)
lista_xd.append([1, 2, 3])  # dodaje jeden nowy elementy list jako całość [1, 2, 3]
print("Dodanie append v2:", lista_xd)
# 1. append(x) - dodaje element na sam koniec listy
# (pokazane wyżej)

# 2. extend(iterable) - dołącza elementy z innej kolekcji na koniec listy
# (pokazane wyżej)

# 3. insert(index, element) - wstawia element pod wskazany indeks
owoce = ["jabłko", "banan", "gruszka"]
print("\n" + "=" * 50)
print("Oryginalna lista owoców:", owoce)
owoce.insert(1, "pomarańcza")  # wstawiamy na indeks 1
print("Po insert(1, 'pomarańcza'):", owoce)

# 4. remove(wartość) - usuwa pierwsze wystąpienie danej wartości
owoce.remove("banan")
print("Po remove('banan'):", owoce)

# 5. pop([indeks]) - usuwa i ZWRACA element z podanego indeksu (domyślnie ostatni: -1)
usuniety_owoc = owoce.pop()  # usuwa ostatni ("gruszka")
print("Po pop():", owoce, "| Zwrócony owoc:", usuniety_owoc)

usuniety_z_indeksu = owoce.pop(0)  # usuwa z indeksu 0 ("jabłko")
print("Po pop(0):", owoce, "| Zwrócony owoc:", usuniety_z_indeksu)

# 6. index(wartość) - zwraca indeks pierwszego wystąpienia wartości
litery = ["a", "b", "c", "d", "b", "e"]
print("\n" + "=" * 50)
print("Lista liter:", litery)
indeks_b = litery.index("b")
print("Indeks pierwszej litery 'b':", indeks_b)

# 7. count(wartość) - zlicza ile razy dany element występuje na liście
ile_razy_b = litery.count("b")
print("Liczba wystąpień 'b':", ile_razy_b)

# 8. sort() - sortuje listę W MIEJSCU (in-place, modyfikuje oryginał i zwraca None)
liczby = [45, 12, 89, 3, 27]
print("\n" + "=" * 50)
print("Liczby przed sortowaniem:", liczby)
liczby.sort()
print("Po liczby.sort():", liczby)

liczby.sort(reverse=True)  # sortowanie malejące
print("Po liczby.sort(reverse=True):", liczby)

# 9. reverse() - odwraca kolejność elementów W MIEJSCU (in-place)
liczby.reverse()
# liczby[::-1]
print("Po liczby.reverse():", liczby)

# 10. copy() - tworzy płytką kopię (shallow copy) listy
liczby_kopia = liczby.copy()
liczby_kopia.append(999)
print("\n" + "=" * 50)
print("Oryginał:", liczby)
print("Kopia po dodaniu 999:", liczby_kopia)

# 11. clear() - usuwa wszystkie elementy z listy
liczby_kopia.clear()
print("Po clear() na kopii:", liczby_kopia)
