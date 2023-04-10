import service.generadorVariablesAleatorias as rng

vector = []
n = 1
for i in range(50000):
    print(n)
    print(rng.distribucionExpNegativa(5))
    n+=1