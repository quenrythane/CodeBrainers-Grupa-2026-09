punkty = 88

# elif - else if
# Program wykonuje tylko jedne instrukcje, i to te pierwsze, które mają True.

if punkty < 50:  # False
    print("nie zdałeś")

elif punkty < 60:  # False
    print("zdałeś na 3")

elif punkty < 70:  # False
    print("zdałeś na 4")

elif punkty < 80:  # False
    print("zdałeś na 5")

elif punkty < 90:  # True
    print("zdałeś na 6")

elif punkty < 100:  # Już nie sprawdzam, bo jestem elif i wyżej było True
    print("zdałeś na 7")

else:  # Już nie sprawdzam, bo jestem else i wyżej było True
    print("punkty poza skalą")