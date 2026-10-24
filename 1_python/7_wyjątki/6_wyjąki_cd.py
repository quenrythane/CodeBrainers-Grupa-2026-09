liczba = 0
# liczba = 1

try:
    wynik = 10 / liczba

except ZeroDivisionError:  # opcjonalnie as błąd
    print(f"Wystąpił błąd ZeroDivisionError")

except Exception as błąd:
    print(f"Wystąpił nieznany błąd : {str(błąd).upper()}")

else:
    print(f"else: Jestem Else i informuje że Try wykonał się poprawnie i wynik to {wynik}")

finally:
    print("finally: Wykonam się zawsze na końcu bo jestem \"finally\"")




