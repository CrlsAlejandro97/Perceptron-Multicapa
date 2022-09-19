import random

class Distorsionador:
    def __init__(self, min_distorsion, max_distorsion):
        self.min_distorsion = min_distorsion
        self.max_distorsion = max_distorsion
    
    def _calcDistorsion(self):
        distorsion = round(random.uniform(self.min_distorsion, self.max_distorsion), 2)
        return distorsion
    
    def distorsionar(self, letras):
        distorsiones = []
        cant_sin_dist = int(0.1 * len(letras))
        for i in range(cant_sin_dist, len(letras)):
            letra = letras[i]
            distorsion = self._calcDistorsion()
            distorsiones.append(distorsion)
            letras[i] = self._dist_letra(letra, distorsion)
        return distorsiones

    def _dist_letra(self, letra, distorsion):
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
    













