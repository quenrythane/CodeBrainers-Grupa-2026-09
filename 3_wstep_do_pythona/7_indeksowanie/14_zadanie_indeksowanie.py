alfabet = "abcdefghijklmnopqrstuvwxyz"

# zwróć 10 pierwszych liter
print("10 pierwszych liter:", alfabet[:10])

# zwróć 5 ostanich liter
print("5 ostatnich liter:", alfabet[-5:])

# zwróć 5 liter zaczynając od litery "i"
# Litera "i" ma indeks 8, bierzemy 5 znaków: od 8 do 8+5 = 13
print("5 liter od 'i':", alfabet[8:13])

# zwróć co drugą literę
print("Co druga litera:", alfabet[::2])

# odwróć cały alfabet.
print("Odwrócony alfabet:", alfabet[::-1])
