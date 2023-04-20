import random
import numpy as np

def generar_datos_aleatorios(n):
    """
    Función que genera 'n' datos aleatorios entre 0 y 1, y luego genera 'n' datos de distribución uniforme
    utilizando los mismos datos aleatorios generados.

    Args:
        n (int): Número de datos a generar.

    Returns:
        tuple: Tupla con dos arrays, el primero contiene los datos aleatorios y el segundo contiene los datos
        de distribución uniforme.
    """
    #valor de truncado
    trunc = 2
    datos_aleatorios = [round(random.random(),trunc) for _ in range(n)]  # Generar datos aleatorios
    datos_uniforme = np.random.uniform(0, 7, size=n)  # Generar datos de distribución uniforme
    datos_truncados= np.round(datos_uniforme,trunc)
    return datos_aleatorios, datos_truncados


def distribucionUniforme(a,b):
    """Generacion de variables aleatorias
    Distribucion uniforme 
    a = extremo minimo, b = extremo maximo"""
    rnd = random.random()
    x = a + (rnd * (b - a))
    return x