'''
1. Stwórz plik conftest.py:

Utwórz nową fixture o nazwie uzytkownik_premium.
Fixture ma zwracać słownik reprezentujący dane testowe klienta
{
    "username": "tester_pro",
    "email": "tester@example.com",
    "is_premium": True,
    "punkty": 120
}


2.
Napisz test jednostkowy o nazwie test_weryfikacja_uzytkownika_premium.
Wstrzyknij do funkcji testowej fixture uzytkownik_premium.
Dodaj asercje (assert) weryfikujące, że:
- Użytkownik posiada status premium (is_premium wynosi True).
- Liczba punktów (punkty) jest większa bądź równa 100.
- Adres email zawiera znak @.


3. Uruchom test

'''