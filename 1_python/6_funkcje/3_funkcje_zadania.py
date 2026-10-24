# zrób funkcje która przyjmuje imię.
# Na baize przyjętego imienia przywitaj się z tą osobą.
# przypilnuj żeby imię było napisane z dużej litery.
# przykład przywitanie("artur") powinno zwrócić "Cześć Artur"
# .capitalize()


def powitanie(imie: str):
    print(f"Cześć {imie.capitalize()}!")


powitanie("adam")
powitanie("KASIA")
powitanie("PaWEl")
