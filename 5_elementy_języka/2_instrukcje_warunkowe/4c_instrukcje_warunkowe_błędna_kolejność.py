punkty = 20

# KOLEJNOŚĆ WARUNKÓW MA ZNACZENIE!
# Tu kolejność jest błędna, przez co zawsze wykona się tylko pierwszy warunek. 
if punkty < 100:  # True
    print("zdałeś na 7")

elif punkty < 90:
    print("zdałeś na 6")

elif punkty < 80:
    print("zdałeś na 5")

elif punkty < 70:
    print("zdałeś na 4")

elif punkty < 60:
    print("zdałeś na 3")

elif punkty < 50:
    print("nie zdałeś")


else:
    print("punkty poza skalą")