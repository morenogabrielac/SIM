from src.widgets.generadorVariablesAleatorias import *
import math


def generar_datos_Distribucion(Distribution, datosDistribucion):
    """
    Función que genera 'n' datos aleatorios entre 0 y 1, y luego genera 'n' datos de distribución uniforme
    utilizando los mismos datos aleatorios generados.

    Args:
        n (int): Número de datos a generar.
        
        Distribution: Tipo de distribucion seleccionanda entre las siguientes [1:Poisson,2:Uniforme,3:Normal,4:Exponencial]
        
        datosDistribucion: aca van a ir los datos que correspondan a las diferentes distribuciones usando el siguiente diccionario
            datos = {
            'Numero de muestra': 0,
            'Varianza': 0,
            'Media': 0,
            'Desviacion Estandar': 0,
            'Lambda': 0,
            'Intervalo Superior': 0,
            'Intervalo Inferior': 0,
            'Cantidad intervalos': 0
        }


    Returns:
        tuple: Tupla con dos arrays, el primero contiene los datos aleatorios y el segundo contiene los datos
        de distribución uniforme.
    """
    #valor de truncado
    #datosDistribucion["Media"]
    datosDistribucion["Varianza"] = datosDistribucion["Desviacion Estandar"] ** 2
    

    if(Distribution==1):
        datos_aleatorios = [math.trunc(distribucionPoisson(1/(datosDistribucion['Lambda'])) * 10000) / 10000 for _ in range(datosDistribucion["Numero de muestra"])]
    elif(Distribution==2):
        datos_aleatorios = [math.trunc(distribucionUniforme(datosDistribucion["Intervalo Inferior"],datosDistribucion["Intervalo Superior"])* 10000)/ 10000 for _ in range(datosDistribucion["Numero de muestra"])]
    elif(Distribution==3):
        datos_aleatorios = [math.trunc(distribucionNormal(datosDistribucion['Media'],datosDistribucion['Desviacion Estandar'])*10000 )/10000 for _ in range(datosDistribucion["Numero de muestra"])]
    elif(Distribution==4):
        datos_aleatorios = [math.trunc(distribucionExpNegativa(datosDistribucion('Lambda'))*10000)/10000 for _ in range(datosDistribucion["Numero de muestra"])]

        
        
        
    return datos_aleatorios



