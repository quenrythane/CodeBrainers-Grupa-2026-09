# print("*" * 100)

# print('Mój ulubiony cytat to "veni, vidi, vici"')
# print("it's a cat")
# print("it's a cat")

# string1 = "string1"
# string2 = 'string2'
# string3 = """ string3 """
# string4 = ''' linjka 1
# linjka 2
# linjka 3 '''

# print("Mój ulubiony cytat to \"veni, vidi, vici\".")


print("\tTo jest mój piekny wiersz\nCo wcale się nie rymuje\nale pokazuje jak można\ndodać wiele linii")
# \t - tabulator
# \n - nowa linia

print("""
        To jest mój piekny wiersz
Co wcale się nie rymuje
ale pokazuje jak można
dodać wiele linii
""")

sciezka = r"C:\Users\natalia\OneDrive\Pulpit"
raw_string = r"to jest surowy string"  # raw string
f_string = f""  # formatowany string

# stwórz 3 zmienne, imie, nazwisko i wiek i przypisz do nich jakieś wartości.
# Następnie przy pomocy printa wydrukuj zdanie: „Nazywam się Artur Wawiński i mam 20 lat.”


imie = "Artur"
nazwisko = "Wawiński"
wiek = 20

# Rozwiązanie główne (rekomendowane): f-string (formatowany string)
print(f"Nazywam się {imie} {nazwisko} i mam {wiek} lat.")
# Alternatywne sposoby (dla porównania):
# 1. Przekazanie jako osobne argumenty (print domyślnie dodaje spacje między argumentami):
# print("Nazywam się", imie, nazwisko, "i mam", wiek, "lat.")
# 2. Konkatenacja stringów (wymaga jawnej konwersji liczby na string przez str() oraz dodania spacji):
# print("Nazywam się " + imie + " " + nazwisko + " i mam " + str(wiek) + " lat.")
