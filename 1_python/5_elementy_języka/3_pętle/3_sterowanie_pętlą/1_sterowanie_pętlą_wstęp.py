
imion = ["Artur", "Bartek", "Celina", "Damian", "Ela", "Felicja", "Grzegorz", "Halina", "Igor", "Irena"]

print("\nTo jest pętla for:")
for imie in imion:
    print(f"Cześć {imie}")

print("\nTo jest continue")
for imie in imion:
    czy_kobieta = imie[-1] == "a"
    if czy_kobieta:
        continue
    print(f"Cześć {imie}")



print("\nTo jest break")
for imie in imion:
    czy_kobieta = imie[-1] == "a"
    if czy_kobieta:
        break
    print(f"Cześć {imie}")