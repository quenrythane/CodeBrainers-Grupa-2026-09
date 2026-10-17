zbiór = {"Artur", "Bartek", "Czarek"}

print(zbiór, "\n")
# zbiór[0] <- To jest niedozwolone na zbiorach.
zbiór.add("Damian")
print("po dodaniu Damiana:", zbiór, "\n")

zbiór.add("Damian")
zbiór.add("Damian")
zbiór.add("Damian")
print("po dodaniu Damiana x3:", zbiór, "\n")


lista = ["Artur", "Bartek", "Czarek", "Damian", "Damian", "Damian"]
print("lista: ", lista, "\n")
lista_bez_powtórzeń = list(set(lista))
print("lista bez powtórzeń: ", lista_bez_powtórzeń, f"o typie {type(lista_bez_powtórzeń)}", "\n")




