import random
from scipy.stats import chi2
import math
tabla_chi = [[1,3.84],[2,5.99],[3,7.81],[4,9.49],[5,11.07],[6,12.59],[7,14.07],[8,15.51],[9,16.92],[10,18.31],[11,19.68],[12,21.03],[13,22.36],[14,23.68],[15,25.00],[16,26.30],[17,27.59],[18,28.87],[19,30.14],[20,31.41],[21,32.67],[22,33.92],[23,35.17],[24,36.42],[25,37.65],[26,38.89],[27,40.11],[28,41.34],[29,42.56],[30,43.77],[40,55.76],[50,67.50],[60,79.08],[70,90.53],[80,101.90],[90,113.10],[100,124.3]]

def distribucionUniforme(a,b):
    """Generacion de variables aleatorias
    Distribucion uniforme 
    a = extremo minimo, b = extremo maximo"""
    rnd = random.random()
    x = a + (rnd * (b - a))
    return x
    

#Distribucion exponencial negativa
#la funcion usa la ecuacion de la media, por lo cual, asegurarse de pasar como parametro la media y no el lambda
#m = media

def distribucionExpNegativa(m):
    rnd = random.random()
    log = math.log(1 - rnd)
    x = -m*log
    return x


#Distribucion normal
#Usa el metodo de Box-Muller
#m = media, desviacion

def distribucionNormal(m,desviacion):
    pi = math.pi
    rnd1 = random.random()
    rnd2 = random.random()
    desviacion = math.sqrt(desviacion)
    x1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * pi * rnd2))*desviacion + m
    x2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * pi * rnd2))*desviacion + m
    aleatorio = random.random()
    if(aleatorio > 0,4999):
        resultado = x1
    else:
        resultado = x2
    
    return resultado

#Distribucion de Poisson
#b = lambda

def distribucionPoisson(b):
    p = 1
    x = -1
    a = math.exp(-b)
    while(p >= a):
        p = p * random.random()
        x = x + 1
    return x


def prueba_chi(nro_dist, intervalos, suma):
    if nro_dist==1:
        grados = intervalos - 1 - 1 #Valores empiricos en la poisson(1)
    elif nro_dist==2:
        grados = intervalos - 1 - 0 #Valores empiricos en la uniforme(2)
    elif nro_dist==3:
        grados = intervalos - 1 - 2 #Valores empiricos en la normal(3)
    elif nro_dist==4:
        grados = intervalos - 1 - 1 #Valores empiricos en la exponencial(4)

    res = False

    for i in tabla_chi:
        if i[0] == grados:
            valor_tabla = i[1]
            
        else:
            valor_tabla = chi2_critical_value(0.95, grados)
    
    if suma <= valor_tabla:
        res = f"Dado que el valor de la C(acu):{suma} <= {valor_tabla}  No se puede rechazar la hipotesis"
    else:
        res = f"Dado que el valor de la C(acu):{suma} > {valor_tabla}  Se rechazar la hipotesis"
        
    
    return res



def chi2_critical_value(confidence_level, df):
    """Calcula el valor crítico de la distribución Chi-Cuadrado para un nivel de confianza y grados de libertad dados"""
    return chi2.ppf(1 - confidence_level, df)


