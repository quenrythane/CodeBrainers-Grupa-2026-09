
def powitanie(imie: str):
    print(f"Cześć {imie.capitalize()}!")


# *args  - arguments
print("\n\nfunckja *args")
def zrób_zakupy(imie, *produkty):
    print(f"zrobie zakupy dla {imie}")
    for produkt in produkty:
        print(f"kupiłem {produkt}")

zrób_zakupy("Pawel", "jablka", "banany", "gruszki", "banany", "gruszki", "banany", "gruszki")


# **kwargs  - keyword arguments (key value arguments)
print("\n\nfunckja **kwargs")
def zrób_zakupy(**produkty):
    # produkty = {
    #     "jablka": 2,
    #     "banany": 3,
    #     "gruszki": 4
    # }
    for produkt, ilosc in produkty.items():  # ("klucz", "wartość")
        print(f"kupiłem {produkt} w ilości {ilosc}")

zrób_zakupy(jablka=2, banany=3, gruszki=4, cytryny=50)

data_json = {
    "name": "pawel",
    "salary": 10_000,
    }


print(data_json.get("name") == "pawel")

