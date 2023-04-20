from src.widgets.generadorVariablesAleatorias import *


def generar_datos_Distribucion(Distribution, datosDistribucion):
    """
    Función que genera 'n' datos aleatorios entre 0 y 1, y luego genera 'n' datos de distribución uniforme
    utilizando los mismos datos aleatorios generados.

    Args:
        n (int): Número de datos a generar.
        
        Distribution: Tipo de distribucion seleccionanda entre las siguientes [1:Poisson,2:Uniforme,3:Normal,4:Exponencial]
        
        datosDistribucion: aca van a ir los datos que correspondan a las diferentes distribuciones usando el siguiente diccionario
            {"muestra":444,"media": 1,"desviacion":0,"lambda":5,"limiteSuperior":20,"limiteInferior":0}

    Returns:
        tuple: Tupla con dos arrays, el primero contiene los datos aleatorios y el segundo contiene los datos
        de distribución uniforme.
    """
    #valor de truncado
    
    if(Distribution==1):
        datos_aleatorios = [round(distribucionPoisson(1/(datosDistribucion["media"])), 4) for _ in range(datosDistribucion["muestra"])]
    elif(Distribution==2):
        datos_aleatorios = [round(distribucionUniforme(datosDistribucion["limiteInferior"],datosDistribucion["limiteSuperior"]), 4) for _ in range(datosDistribucion["muestra"])]
    elif(Distribution==3):
        datos_aleatorios = [round(distribucionNormal(datosDistribucion["media"],datosDistribucion["varianza"]) , 4) for _ in range(datosDistribucion["muestra"])]
    elif(Distribution==4):
        datos_aleatorios = [round(distribucionExpNegativa(datosDistribucion("media")), 4) for _ in range(datosDistribucion["muestra"])]

        
        
        
    return datos_aleatorios



