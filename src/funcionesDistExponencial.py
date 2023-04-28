from cmath import exp, pi
from logging import root
import math
import random
import decimal





#Entra como parametro el vector donde estan almacenadas las variables aleatorias y la cantidad de intervalos
#Importante!!!!!!!
#Esta funcion deveulve mas de un valor, por eso a la hora de ejecutarla se debera ejecutar de la siguiente forma:
#   vector1,vector2,vector3,vector4,vector5,numero1,numero2 = distribucion_Densidad(vectorVariablesAleatorias,cantidadIntervalos)
#Para mas especificidad, ver el comentario que esta en el return de la funcion, ahi esta explicada cada devolucion
def distribucion_Densidad(vectorVariablesAleatorias,cantidadIntervalos):
    gradosLibertad = cantidadIntervalos - 2
    N = len(vectorVariablesAleatorias)
    minimoValor = min(vectorVariablesAleatorias)
    maximoValor = max(vectorVariablesAleatorias)
    diferencia = maximoValor - minimoValor
    anchoIntervalos = (diferencia/cantidadIntervalos) + 0.01
    acumuladorMedia = 0 
    #Calculamos la media para la sucesion numerica del vector de variables aleatorias
    for i in range(len(vectorVariablesAleatorias)):
        acumuladorMedia += vectorVariablesAleatorias[i]      
    media = acumuladorMedia/N
    #Calculamos lambda
    lambd = 1/media
    
    #Creamos el vector que va a contener el inicio y fin de cada intervalo
    vectorIntervalosInicioFin = [0] * cantidadIntervalos * 2
    for i in range(len(vectorIntervalosInicioFin)):
        if(i == 0):
            vectorIntervalosInicioFin[i] = minimoValor
            continue
        elif(i == 1):
            vectorIntervalosInicioFin[i] = minimoValor + (anchoIntervalos)
            continue
        elif(i%2 != 0):
            vectorIntervalosInicioFin[i] = vectorIntervalosInicioFin[i - 1] + (anchoIntervalos)
            continue
        else:
            vectorIntervalosInicioFin[i] = vectorIntervalosInicioFin[i - 2] + anchoIntervalos
            continue
        
    
    
    
    #Creamos el vector que va a tener las marcas de clase de cada intervalo
    vectorMarcasDeClase = [0] * cantidadIntervalos
    subIndice1 = 0
    subindice2 = 0
    while(subindice2 < len(vectorIntervalosInicioFin)):
        vectorMarcasDeClase[subIndice1] = (vectorIntervalosInicioFin[subindice2 + 1] + vectorIntervalosInicioFin[subindice2])/2
        subindice2 += 2
        subIndice1 += 1
    #Creamos el vector que va a contener la frecuencia observada en cada intervalo
    vectorFrecuenciaObservada = [0] * cantidadIntervalos
    subindice3 = 1
    subindice4 = 0
    for i in range(len(vectorVariablesAleatorias)):
        while(subindice3 < len(vectorIntervalosInicioFin)):
            if(vectorVariablesAleatorias[i] < vectorIntervalosInicioFin[subindice3]):
                vectorFrecuenciaObservada[subindice4] += 1
                subindice3 = 1
                subindice4 = 0
                break
            else:
                subindice3 += 2
                subindice4 += 1
    
    
    #Calculamos la distribucion de densidad y la frecuencia esperada para cada intervalo
    vectorDistribucionDensidadcmc = [0] * cantidadIntervalos
    vectorDistribucionDensidadcPac = [0] * cantidadIntervalos
    vectorFrecuenciaEsperada = [0] * cantidadIntervalos
    subindice5 = 1
    acumuladorPo = 0
    for i in range(len(vectorDistribucionDensidadcPac)):
        
        vectorDistribucionDensidadcPac[i] = (1-math.exp(-lambd*vectorIntervalosInicioFin[subindice5])-(1-math.exp(-lambd*vectorIntervalosInicioFin[subindice5 -1])))
        vectorDistribucionDensidadcmc[i] = lambd*math.exp(-lambd*vectorMarcasDeClase[i])*(vectorIntervalosInicioFin[subindice5]-vectorIntervalosInicioFin[subindice5 -1])
        vectorFrecuenciaEsperada[i] = vectorDistribucionDensidadcPac[i] * N
        subindice5 += 2
        acumuladorPo += vectorDistribucionDensidadcPac[i]
       
    
    #En este loop, lo que hacemos es agrupar con los intervalos adyacentes, aquellos intervalos que tengan una frecuencia esperada menos a 5
    for i in range(len(vectorFrecuenciaEsperada)):
        if(vectorFrecuenciaEsperada[i] < 5):
            if(i == len(vectorFrecuenciaEsperada) - 1):
                vectorFrecuenciaEsperada[i - 1] += vectorFrecuenciaEsperada[i]
                vectorFrecuenciaObservada[i - 1] += vectorFrecuenciaObservada[i]
                vectorFrecuenciaObservada[i] = 0
                vectorFrecuenciaEsperada[i] = 0
                vectorIntervalosInicioFin[(i*2)] = 0
                vectorIntervalosInicioFin[(i*2)-1] = 0
                if(vectorFrecuenciaEsperada[i - 1] < 5):
                    subindice6 = 1
                    while(vectorFrecuenciaEsperada[i - subindice6] < 5):
                        vectorFrecuenciaEsperada[(i - subindice6) - 1] += vectorFrecuenciaEsperada[i - subindice6]
                        vectorFrecuenciaObservada[(i - subindice6) - 1] += vectorFrecuenciaObservada[i - subindice6]
                        vectorFrecuenciaObservada[(i - subindice6)] = 0
                        vectorFrecuenciaEsperada[(i - subindice6)] = 0
                        vectorIntervalosInicioFin[((i - subindice6)*2)] = 0
                        vectorIntervalosInicioFin[((i - subindice6)*2)-1] = 0
                        subindice6 += 1

            else:
                vectorFrecuenciaEsperada[i + 1] += vectorFrecuenciaEsperada[i]
                vectorFrecuenciaEsperada[i] = 0
                vectorFrecuenciaObservada[i + 1] += vectorFrecuenciaObservada[i]
                vectorFrecuenciaObservada[i] = 0
                
                if(i==0):
                    vectorIntervalosInicioFin[1] = 0
                    vectorIntervalosInicioFin[2] = 0
                else:
                    vectorIntervalosInicioFin[(i*2)+1] = 0
                    vectorIntervalosInicioFin[(i*2)+2] = 0
    
    
    #Aqui calculamos el C de chi cuadrado y el Cac(C acumulado) para cada intervalo
    acumuladorCChiCuadrado = 0
    vectorCChiCuadrado = [0] * len(vectorFrecuenciaObservada)
    for i in range(len(vectorFrecuenciaObservada)):
        if(vectorFrecuenciaObservada[i] == 0):
            vectorCChiCuadrado[i] = 0
        else:
            vectorCChiCuadrado[i] = ((vectorFrecuenciaObservada[i] - vectorFrecuenciaEsperada[i])**2)/vectorFrecuenciaEsperada[i]
            acumuladorCChiCuadrado += vectorCChiCuadrado[i]
    
    #Debemos calcular nuevamente los grados de libertad porque ahora la cantidad de intervalos cambio
    cantidadNuevaDeIntervalos = 0
    for i in range(len(vectorFrecuenciaObservada)):
        if(vectorFrecuenciaObservada[i] != 0):
            cantidadNuevaDeIntervalos += 1
    gradosLibertad = cantidadNuevaDeIntervalos - 2
        

    #Esta funcion retorna de forma secuencial lo siguiente:
    #   vectorIntervalosInicioFin: Este vector ya esta modificado para la forma de chi cuadrado,
    # es decir que muchos de los intervalos se agruparon con su adyacente, por lo cual, todas las celdas que esten en 0 son limites
    # de intervalos que fueron eliminados para formar los nuevos intervalos mas grandes
    #   vectorIntervalosInicioFin: AL igual que el anterior, este vector ya esta modificado para la forma de chi cuadrado, 
    # por lo cual algunas de las celdas son 0, siendo estas las pertenecientes a los antiguos intervalos que no superaban una 
    # distribucion de densidad mayor o igual a 5
    #   vectorFrecuenciaObservada:Exactamente igual que los dos anteriores
    #   vectorFrecuenciaEsperada:Igual a los anteriores
    #   vectorCChiCuadrado:Este vector contiene los valores de c para cada intervalo, los que son 0 son para los intervalos que 
    # ya no existen, por lo tanto, no tienen significado
    #   acumuladorCChiCuadrado:Este es el valor que vamos a comparar con la tabla de chi cuadrado
    #   gradosLibertad:Grados de libertad que tenemos
    vector = list(map(lambda x: decimal.Decimal(x).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN), vector))
   

    
    return vectorIntervalosInicioFin,vectorDistribucionDensidadcmc, vectorDistribucionDensidadcPac, vectorFrecuenciaObservada, vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad
    




def distribucion_DensidadBase(vectorVariablesAleatorias,cantidadIntervalos):
    
    N = len(vectorVariablesAleatorias)
    minimoValor = min(vectorVariablesAleatorias)
    maximoValor = max(vectorVariablesAleatorias)
    diferencia = maximoValor - minimoValor
    anchoIntervalos = (diferencia/cantidadIntervalos) + 0.01
    acumuladorMedia = 0 
    #Calculamos la media para la sucesion numerica del vector de variables aleatorias
    for i in range(len(vectorVariablesAleatorias)):
        acumuladorMedia += vectorVariablesAleatorias[i]      
    media = acumuladorMedia/N
    #Calculamos lambda
    lambd = 1/media
    
    #Creamos el vector que va a contener el inicio y fin de cada intervalo
    vectorIntervalosInicioFin = [0] * cantidadIntervalos * 2
    for i in range(len(vectorIntervalosInicioFin)):
        if(i == 0):
            vectorIntervalosInicioFin[i] = minimoValor
            continue
        elif(i == 1):
            vectorIntervalosInicioFin[i] = minimoValor + (anchoIntervalos)
            continue
        elif(i%2 != 0):
            vectorIntervalosInicioFin[i] = vectorIntervalosInicioFin[i - 1] + (anchoIntervalos)
            continue
        else:
            vectorIntervalosInicioFin[i] = vectorIntervalosInicioFin[i - 2] + anchoIntervalos
            continue
        
    
    
    
    #Creamos el vector que va a tener las marcas de clase de cada intervalo
    vectorMarcasDeClase = [0] * cantidadIntervalos
    subIndice1 = 0
    subindice2 = 0
    while(subindice2 < len(vectorIntervalosInicioFin)):
        vectorMarcasDeClase[subIndice1] = (vectorIntervalosInicioFin[subindice2 + 1] + vectorIntervalosInicioFin[subindice2])/2
        subindice2 += 2
        subIndice1 += 1
    #Creamos el vector que va a contener la frecuencia observada en cada intervalo
    vectorFrecuenciaObservada = [0] * cantidadIntervalos
    subindice3 = 1
    subindice4 = 0
    for i in range(len(vectorVariablesAleatorias)):
        while(subindice3 < len(vectorIntervalosInicioFin)):
            if(vectorVariablesAleatorias[i] < vectorIntervalosInicioFin[subindice3]):
                vectorFrecuenciaObservada[subindice4] += 1
                subindice3 = 1
                subindice4 = 0
                break
            else:
                subindice3 += 2
                subindice4 += 1
    
    
    #Calculamos la distribucion de densidad y la frecuencia esperada para cada intervalo
    gradosLibertad = cantidadIntervalos - 2
    vectorDistribucionDensidadcmc = [0] * cantidadIntervalos
    vectorDistribucionDensidadcPac = [0] * cantidadIntervalos
    vectorFrecuenciaEsperada = [0] * cantidadIntervalos
    subindice5 = 1
    acumuladorPo = 0
    for i in range(len(vectorDistribucionDensidadcPac)):
        
        vectorDistribucionDensidadcPac[i] = (1-math.exp(-lambd*vectorIntervalosInicioFin[subindice5])-(1-math.exp(-lambd*vectorIntervalosInicioFin[subindice5 -1])))
        vectorDistribucionDensidadcmc[i] = lambd*math.exp(-lambd*vectorMarcasDeClase[i])*(vectorIntervalosInicioFin[subindice5]-vectorIntervalosInicioFin[subindice5 -1])
        vectorFrecuenciaEsperada[i] = vectorDistribucionDensidadcPac[i] * N
        subindice5 += 2
        acumuladorPo += vectorDistribucionDensidadcPac[i]
    
    return vectorMarcasDeClase,vectorDistribucionDensidadcmc,vectorIntervalosInicioFin, vectorDistribucionDensidadcPac, vectorFrecuenciaObservada, vectorFrecuenciaEsperada,gradosLibertad
    


#vectorIntervalosInicioFin,vectorDistribucionDensidadcmc, vectorDistribucionDensidadcPac, vectorFrecuenciaObservada, vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad = distribucion_Densidad(vector,10)
#vectorMarcasDeClaseBase,vectorDistribucionDensidadcmcBase,vectorIntervalosInicioFinBase, vectorDistribucionDensidadcPacBase, vectorFrecuenciaObservadaBase, vectorFrecuenciaEsperadaBase = distribucion_DensidadBase(vector,10)

