from Equation import Expression

from algorithms import newton_mas_secante
from exceptions import validate_err, validate_range

msg =  """
 _________________________________
|                                 |
| METODO SECANTE + NEWTON-RAPHSON |
|_________________________________|

  INTEGRANTES:
  |_ Loana Abril Schleich Garcia.

  FUNCION A EVALUAR:
  |_ f(x) = x^(3)-6x^(2)+11x-6
    |_ f'(x) = 3x^(2)-12x+11
        """

print(msg)

# Defino la función y su derivada como una expresión simbólica.
fx = Expression('x^(3)-6x^(2)+11x-6', ['x'])
fxp = Expression('3x^(2)-12x+11', ['x'])

# Pido rango inicial de búsqueda y una cota de error.
# No importa el orden de los valores en el rango (x0 > x1 y x1 >0 son rangos válidos).
# La cota de error no puede ser menor a cero (validado).
print('RANGO INICIAL DE BUSQUEDA:')
x0 = float(input('|_ x0: '))
x1 = float(input('|_ x1: '))
validate_range(x0, x1) # Valido que el rango sea válido.
err = float(input("MARGEN DE ERROR: "))
validate_err(err, 'MARGEN DE ERROR') # Valido que el margen de error sea mayor a cero.

# Se verifica que ninguno de los valores de x proporcionados sea una raíz de la función.
print() # Hago salgo de línea
if(fx(x0) == 0):
    print(f"El valor proporcionado {x0} es una raíz")
elif(fx(x1) == 0):
    print(f"El valor proporcionado {x1} es una raíz")
else :
    #Se imprimen los valores recibidos en caso de que no lo sean
    tabla, raiz = newton_mas_secante(fx, fxp, x0, x1, err)

    print(tabla)
    print("\nAproximación final de la raíz: ", raiz)
    print("Evaluación de la raíz hallada en f(x): " + str(fx(raiz)))
