
owoce = ["Arbuz", "Banan", "Cytryna", "Daktyle", "Eszalotka", "Figi", "Grejpfrut", "Hebanowiec", "Imbir", "Jaglanki"]

# Stwórz pęle for która printuej nazwe owocu.
# używając instrukcji continue omijaj print owocu który ma wiecej niż 5 liter

for owoc in owoce:
    if len(owoc) > 5:
        continue
    print(owoc)


for owoc in owoce:
    pass

print("inny kawałek kodu")
