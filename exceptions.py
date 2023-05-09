#Lanza un error si el número es negativo
def is_positive(numero, campo):
    if(is_negative(numero)):
        raise NegativeNumber(campo)

class NegativeNumber(Exception):
    def __init__(self, campo):
        super().__init__(f"El campo numérico {campo} debe ser positivo.")

def is_negative(value):
    return True if(value < 0) else False



