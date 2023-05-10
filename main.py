from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from Equation import Expression

from algorithms import newton_mas_secante
from exceptions import validate_err

msg =  """
 _________________________________________________________________________________________________________________________
|                                                                                                                         |
|                                          METODO SECANTE + NEWTON-RAPHSON                                                |
|_________________________________________________________________________________________________________________________|
|                                                                                                                         |
|  INTEGRANTES:                                                                                                           |
|  |_ Loana Abril Schleich Garcia.                                                                                        |
|                                                                                                                         |
|  FUNCION A EVALUAR:                                                                                                     |
|  |_ f(x) = x^(3)-6x^(2)+11x-6                                                                                           | 
|_________________________________________________________________________________________________________________________|
|                                                                                                                         |
|                                              FUNCIONAMIENTO DEL ALGORITMO                                               |
|_________________________________________________________________________________________________________________________|
|                                                                                                                         |
|  Para encontrar la raíz de una función, se utilizan dos métodos: el método de la secante y el de Newton-Raphson.        |
|                                                                                                                         |
|  El método de la secante necesita dos valores iniciales del eje x, que son las dos primeras aproximaciones de la raíz.  |
|  A partir de estos valores, se realizan los cálculos necesarios para obtener una primera aproximación de la raíz.       |
|                                                                                                                         |
|  Luego, se utiliza esta primera aproximación como valor inicial para el método de Newton-Raphson,                       |
|  que requiere un valor inicial del eje x y la derivada de la función. Con estos datos,                                  |
|  se obtiene una nueva aproximación de la raíz.                                                                          |
|                                                                                                                         |
|  Ambos métodos generan dos aproximaciones de la raíz, que son utilizadas como las dos primeras                          |
|  aproximaciones de x en la siguiente iteración. En resumen, se comienza con dos valores iniciales                       |
|  arbitrarios (semillas), se genera una nueva aproximación de la raíz a partir de estos valores,                         |
|  esta nueva aproximación se utiliza como semilla para el segundo método, que produce una mejor aproximación.            |
|  Ambos resultados se utilizan como semillas para la siguiente iteración.                                                |
|_________________________________________________________________________________________________________________________|        
        
          """

print(msg)

# Defino la función y su derivada como una expresión simbólica.
fx = Expression('x^(3)-6*x^(2)+11*x-6', ['x'])
fxp = Expression('3*x^(2)-12*x+11', ['x'])

# Pido rango inicial de búsqueda y una cota de error.
# No importa el orden de los valores en el rango (x0 > x1 y x1 >0 son rangos válidos).
# La cota de error no puede ser menor a cero (validado).
print('APROXIMACIONES INICIALES DE BUSQUEDA:')
x0 = float(input('|_ x0: '))
x1 = float(input('|_ x1: '))

err = float(input("MARGEN DE ERROR: "))
validate_err(err, '[MARGEN DE ERROR]') # Valido que el margen de error sea mayor a cero.

raiz = 0

# Se verifica que ninguno de los valores de x proporcionados sea una raíz de la función.
print() # Hago salgo de línea
if(fx(x0) == 0):
    print(f"La aproximación inicial {x0} es una raíz")
    raiz = x0
elif(fx(x1) == 0):
    print(f"La aproximación inicial {x1} es una raíz")
    raiz = x1
else :
    #Se imprimen los valores recibidos en caso de que no lo sean
    tabla, raiz = newton_mas_secante(fx, fxp, x0, x1, err)

    print(tabla.to_string(index = False))
    print("\nAproximación final de la raíz: ", raiz)
    print("Evaluación de la raíz hallada en f(x): " + str(fx(raiz)))

# Genero gráfico de la función, con la raíz evaluada en la función
x = np.linspace(raiz-4, raiz+4, 300)
fig, ax = plt.subplots()
ax.plot(x, fx(x), 'k')
ax.scatter(raiz, fx(raiz), color='r')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray') 
plt.title('Raíz evaluada en f(x)')

plt.show()