
import decimal
import math

def poisson_densidad(rango_numeros, lambd):
    densidades = []
    for k in rango_numeros:
        densidad = math.exp(-lambd) * pow(lambd, k) / math.factorial(k)
        densidades.append(densidad)
        
    densidades = list(map(lambda x: decimal.Decimal(x).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN), densidades))
    return densidades

def analizar_numeros(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    rango_numeros = range(minimo, maximo+1)
    frecuencias = [0] * len(rango_numeros)
    for n in numeros:
        indice = n - minimo
        frecuencias[indice] += 1
    return rango_numeros, frecuencias

def calcular_frecuencia_esperada(frecuencia, tam_muestra):
    frec_esperada = []
    for n in frecuencia:
        calculo = n * tam_muestra
        frec_esperada.append(calculo)
        
    frec_esperada = list(map(lambda x: decimal.Decimal(x).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN), frec_esperada))
    return frec_esperada