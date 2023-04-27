
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
        
    frec_esperada = [math.ceil(n) for n in frec_esperada]
    #frec_esperada = list(map(lambda x: decimal.Decimal(x).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN), frec_esperada))
    return frec_esperada

def analizar_frecuencias(valor, frecuencia_esperada, frecuencia_observada):
    frecuencia_esperada_analizada = []
    frecuencia_observada_analizada = []
    valor_analizado = []
    suma_esperada = 0
    suma_observada = 0
    indices = []
    
    for i, (freq_e, freq_o) in enumerate(zip(frecuencia_esperada, frecuencia_observada)):
        suma_esperada += freq_e
        suma_observada += freq_o
        indices.append(i)
        if suma_esperada >= 5:
            # suma_esperada las frecuencias y agrega el valor a la lista
            frecuencia_esperada_analizada.append(suma_esperada)
            frecuencia_observada_analizada.append(suma_observada)
            valor_analizado.append([valor[j] for j in indices])
            suma_esperada = 0
            suma_observada = 0
            indices = []
    
    # si quedaron elementos sin agrupar, agréguelos al final
    if suma_esperada > 0 and suma_esperada >= 5:
        
        frecuencia_esperada_analizada.append(suma_esperada)
        frecuencia_observada_analizada.append(suma_observada)
        valor_analizado.append([valor[j] for j in indices])
        
    else:
        ultimo_indice = len(valor_analizado) - 1       
        ultimo_valor_actual = valor_analizado[ultimo_indice]        
        valores_restantes = [valor[j] for j in indices]
        valor_analizado[ultimo_indice]=ultimo_valor_actual + valores_restantes
        frecuencia_esperada_analizada[ultimo_indice] = frecuencia_esperada_analizada[ultimo_indice] + suma_esperada
        frecuencia_observada_analizada[ultimo_indice] = frecuencia_observada_analizada[ultimo_indice] + suma_observada 
        
        
        

    return valor_analizado, frecuencia_esperada_analizada, frecuencia_observada_analizada
    
def calcular_estadistico_discreto(fe,fo):
    c = []
    
    for fe_selected, fo_selected in zip(fe,fo):
        resultado = ((fe_selected - fo_selected)**2)/ fe_selected
        c.append(resultado)
    c = list(map(lambda x: decimal.Decimal(x).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN), c))    
    return c

def calcular_estadistico_acumulado(c):
    
    suma = 0
    for valor in c:
        suma += valor
    return suma