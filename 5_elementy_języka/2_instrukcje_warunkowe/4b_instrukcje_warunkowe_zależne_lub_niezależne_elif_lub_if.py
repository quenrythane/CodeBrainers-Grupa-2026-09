punkty = 88

# elif - else if
# Tutaj kolejność jest poprawna.
# Ale są tutaj same indywidualne 'if' co sprawia, że są to instrukcje niezależne.
# Co jest poprawną metodą pisania kodu, ale tylko wtedy, gdy instrukcje są niezależne.
# W tym przypadku przez to że ify są niezależne, zostaną zwrócone 2 oceny: 6 oraz 7


if punkty < 50:
    print("nie zdałeś")

if punkty < 60:
    print("zdałeś na 3")

if punkty < 70:
    print("zdałeś na 4")

if punkty < 80:
    print("zdałeś na 5")

if punkty < 90:  # True
    print("zdałeś na 6")

if punkty < 100:  # też True
    print("zdałeś na 7")

else:
    print("punkty poza skalą")