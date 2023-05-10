#Lanza un error si el número es negativo
def validate_err(value, field):
    if(value < 0):
        raise NegativeNumber(field)

class NegativeNumber(Exception):
    def __init__(self, campo):
        super().__init__(f"El campo numérico {campo} debe ser positivo.")


