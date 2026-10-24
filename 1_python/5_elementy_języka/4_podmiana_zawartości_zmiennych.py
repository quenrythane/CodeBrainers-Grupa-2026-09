# zajęte_miejsce, imie = (0, 'Artur')


duża_liczba = 1
mała_liczba = 9_000


print("\nPrzed zmianą")
print(f"Duża liczba to {duża_liczba}")
print(f"Mała to {mała_liczba}")

mała_liczba, duża_liczba = duża_liczba, mała_liczba

print("\nPo zmianie")
print(f"Duża liczba to {duża_liczba}")
print(f"Mała to {mała_liczba}")

imie_1, imie_2, imie_3 = "Ania", "Bartek", "Celina"  # Ilość zmiennych i wartości musi się zgadzać.
# imie_1, imie_2, imie_3 = "Ania", "Bartek"
# imie_1, imie_2 = "Ania", "Bartek", "Celina"

print("\nImiona")
print(f"1. imie_1 to {imie_1}")
print(f"2. imie_2 to {imie_2}")
print(f"3. imie_3 to {imie_3}")


imie_1, imie_2, *reszta_imion = ["Ania", "Bartek", "Celina", "Dawid", "Eliza"]

print("\nImiona part2")
print(f"1. imie_1 to {imie_1}")
print(f"2. imie_2 to {imie_2}")
print(f"3. reszta_imion to {reszta_imion}")

imie_pierwsze, *reszta_imion, imie_ostatnie = ["Ania", "Bartek", "Celina", "Dawid", "Eliza"]

print("\nImiona part3")
print(f"1. imie_pierwsze to {imie_pierwsze}")
print(f"2. imie_ostatnie to {imie_ostatnie}")
print(f"3. reszta_imion to {reszta_imion}")





