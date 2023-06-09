from Equation import Expression
import pandas as pd
from sympy import diff, symbols

# Combina los algoritmos de la secante y newton-raphson
def newton_mas_secante(fx, fxp, x0, x1, err):
    datos = pd.DataFrame(columns = [
        'Iteración',
        'Valores Intermedios',
        'Raíz Aproximada',
        'Método Aplicado'
        ])
    
    err = margen_menor_a_error_absoluto(err, x0, x1) # Si la cota es inicialmente menor al error absoluto le asigno ese valor para que se ejecute el bucle
    
    c = 1 # Contador de la iteración
    condicion = lambda p0, p1 : error_absoluto(p0,p1) < err or error_absoluto(p0,p1) == 0 or fx(p0) == 0 or fx(p1) == 0 # Condicion de parada
    while(not condicion(x0,x1)):
        datos, x0, x1 = secante(datos,fx, x0, x1, c) # Recibe datos actualizados y nuevo x0, x1
        c += 1

        # Verifica la condición para el cálculo anterior
        if(condicion(x0,x1)):
            break
        
        datos, x0, x1 = newtonraphson(datos,fx,fxp,x1,c) # Recibe datos actualizados y nuevo x0, x1
        c += 1

    return (datos, x1)

def derivada(fx):
    x = symbols('x')
    return diff(fx, x)

def newtonraphson(df,fx,fxp,p0,count):
    p1 = p0 - (fx(p0))/fxp(p0)

    df = actualizar_dataframe(df, count, round(p0,4), round(p1,4), 'Newton-Raphson')

    return (df, p0, p1)

def secante(df,fx,p0,p1,count):
    dividendo = fx(p1) - fx(p0)

    # Para evitar una división por cero se le suma una cantidad mínima al dividendo
    # en caso de ser cero para evitar errores pero a la vez no perjudicar el cálculo.
    if(dividendo == 0):
        dividendo = 10**-10

    p2 = p1 - (fx(p1)*(p1-p0)) / dividendo

    df = actualizar_dataframe(df, count, "({},{})".format(round(p0,4),round(p1,4)), round(p2,4), 'Secante')

    return (df, p1,p2)

def error_absoluto(x0, x1):
    return abs(x1 - x0)

def actualizar_dataframe(df, iter, puntos, raiz, funcion):
    dic = pd.DataFrame({
        'Iteración': iter,
        'Valores Intermedios': puntos,
        'Raíz Aproximada': raiz,
        'Método Aplicado': funcion
    } , index = range(1))
   
    return pd.concat([df, dic], axis = 0, ignore_index = True)

def margen_menor_a_error_absoluto(err, x0, x1):
    err_abs = error_absoluto(x0,x1)
    return err_abs if(err_abs <= err) else err


    
    