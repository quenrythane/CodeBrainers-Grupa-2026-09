
def pitagoras(a, b):
    return (a ** 2 + b ** 2) ** 0.5

print(pitagoras(3, 4))


print((lambda a, b: (a ** 2 + b ** 2) ** 0.5)(3, 4))

[].sort(key=lambda x: x)



lista_liczb = [1, 2, 3, 4, 5]

lista_kwadratow = []
for liczba in lista_liczb:
    lista_kwadratow.append(liczba ** 2)

print(lista_kwadratow)
print("list comprehension:", [liczba ** 2 for liczba in lista_liczb])


lista_kwadratow.clear()
for liczba in lista_liczb:
    if liczba % 2 == 0:
        lista_kwadratow.append(liczba ** 2)
print(lista_kwadratow)
print("list comprehension:", [liczba ** 2 for liczba in lista_liczb if liczba % 2 == 0])

lista_kwadratow.clear()
for liczba in lista_liczb:
    if liczba % 2 == 0:
        lista_kwadratow.append(liczba ** 2)
    else:
        lista_kwadratow.append("pomidor")
print(lista_kwadratow)
print("list comprehension:", [liczba ** 2 if liczba % 2 == 0 else "pomidor" for liczba in lista_liczb])

print("list comprehension:", [liczba ** 2 if liczba % 2 == 0 else "pomidor" for liczba in lista_liczb if liczba > 2])





