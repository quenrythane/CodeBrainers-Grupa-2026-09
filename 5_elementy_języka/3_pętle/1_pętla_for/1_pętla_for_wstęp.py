
imiona = ["Artur", "Basia", "Celina", "Dawid", "Eliza", "Artur", "Basia", "Celina", "Dawid", "Eliza"]

# DRY - dont repeat yourself
"""
print(f"Witaj {imiona[0]}!")
print(f"Witaj {imiona[1]}!")
print(f"Witaj {imiona[2]}!")
print(f"Witaj {imiona[3]}!")
print(f"Witaj {imiona[4]}!")
print(f"Witaj {imiona[5]}!")
print(f"Witaj {imiona[6]}!")
print(f"Witaj {imiona[7]}!")
print(f"Witaj {imiona[8]}!")
print(f"Witaj {imiona[9]}!")
"""

for imie in imiona:

    print(f"Witaj {imie.upper()}!")

    print(f"Twoje imię ma długość {len(imie)} liter!")

    print("*" * 50)

print("Koniec pętli")

