import random
import math


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
#m = media, v = varianza

def distribucionNormal(m,v):
    pi = math.pi
    rnd1 = random.random()
    rnd2 = random.random()
    x1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * pi * rnd2))*m + v
    x2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * pi * rnd2))*m + v
    return x1,x2

#Distribucion de Poisson
#b = lambda, lambda es la media

def distribucionPoisson(b):
    p = 1
    x = -1
    a = math.exp(-b)
    while(p >= a):
        p = p * random.random()
        x = x + 1
    return x


