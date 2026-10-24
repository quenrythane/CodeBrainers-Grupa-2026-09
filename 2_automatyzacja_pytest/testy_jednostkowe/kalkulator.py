
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    except TypeError:
        raise TypeError("unsupported operand type(s) for /: 'str' and 'int'")
    except ValueError:
        raise ValueError("unsupported operand type(s) for /: 'str' and 'int'")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")