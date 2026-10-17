lista_imion_1 = ["Czarek", "Darek", "Ela", "Artur", "Bartek"]
lista_imion_2 = ["Czarek", "Darek", "Ela", "Artur", "Bartek"]

# print(reversed(lista_imion))

""" Funkcja zwraca nową listę,
natomiast metoda edytuje pierwszą, pierwotną listę.   """
wynik = sorted(lista_imion_1)
wynik_odwrocony = sorted(lista_imion_1, reverse=True)
odwr_wynik = reversed(lista_imion_1)
lista_imion_2.sort()
# lista_imion_2.sort(reverse=True)

print("lista_imion_1", lista_imion_1)
print("lista_imion_2", lista_imion_2)
print("wynik", wynik)
print()

"""
iterowalny_obiekt
enumerate - zwraca indeks i wartość elementu
"""
print("enumerate", list(enumerate("Artur")))
print("enumerate", list(enumerate(lista_imion_2)))

print(len([(0, 'Artur'), (1, 'Bartek'), (2, 'Czarek'), (3, 'Darek'), (4, 'Ela')]))




