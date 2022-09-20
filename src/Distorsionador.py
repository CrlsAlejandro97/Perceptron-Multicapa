import random

class Distorsionador:
    def __init__(self, min_distorsion, max_distorsion):
        self.min_distorsion = min_distorsion
        self.max_distorsion = max_distorsion
    
    def _calcDistorsion(self):

        # Se calcula la distorsion que va a tener la letra en un rangon de min_distorsion a max_distorsion
        distorsion = round(random.uniform(self.min_distorsion, self.max_distorsion), 2)
        return distorsion
    
    def distorsionar(self, letras):
        distorsiones = []

        # El 10% de las letras tienen que mantenerse originales
        cant_sin_dist = int(0.1 * len(letras))
        for i in range(len(letras)):
            if i > int(cant_sin_dist):
                letra = letras[i]
                distorsion = self._calcDistorsion()
                letras[i] = self._dist_letra(letra, distorsion)
            else:
                distorsion = 0
            distorsiones.append(distorsion)
        return distorsiones

    def _dist_letra(self, letra, distorsion):

        # Recorro el arreglo de la letra y si hay un uno hay una probabilidad de un x porciento de que se cambie de lugar dependiendo de la distorsion calculada
        
        for i in range(len(letra)):
            if letra[i] == 1:
                if random.random() < distorsion:
                    num = letra[i]
                    posicion_reemplazo = random.randint(0, 99)
                    while letra[posicion_reemplazo] == 1:
                        posicion_reemplazo = random.randint(0, 99)
                    letra[i] = letra[posicion_reemplazo]
                    letra[posicion_reemplazo] = num
        return letra
    













