#Lanza un error si el número es negativo
def validate_err(value, field):
    if(value < 0):
        raise NegativeNumber(field)

def validate_range(x0, x1):
    is_it_a_range(x0, x1)
    is_range_valid(x0, x1)

def is_range_valid(x0, x1):
    if(x0 > x1):
        raise InvalidRangeValues("El primer campo del rango inicial debe ser menor al segundo.")

def is_it_a_range(x0, x1):
    if(x0 == x1):
        raise InvalidRangeValues("Los campos del rango inicial deben ser distintos.")


class NegativeNumber(Exception):
    def __init__(self, campo):
        super().__init__(f"El campo numérico {campo} debe ser positivo.")


class InvalidRangeValues(Exception):
    pass

