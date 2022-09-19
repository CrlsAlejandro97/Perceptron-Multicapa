import pandas as pd
import numpy as np
import random
from Interfaz import Interfaz

#Guardo las distorsiones para ir mostrando cuanta distorsion tiene cada letra
#Ver como manejar mejor esto
distorsiones = []

class Distorsionador:
    def __init__(self, min_distorsion, max_distorsion):
        self.min_distorsion = min_distorsion
        self.max_distorsion = max_distorsion
    
    def _calcDistorsion(self):
        distorsion = round(random.uniform(self.min_distorsion, self.max_distorsion), 2)
        return distorsion
    
    def distorsionar(self, letras):
        for i in range(len(letras)):
            letra = letras[i]
            letras[i] = self._dist_letra(letra)

    def _dist_letra(self, letra):
        for i in range(len(letra)):
            distorsion = self._calcDistorsion()
            distorsiones.append(distorsion)
            if random.random() < distorsion and letra[i] == 1:
                num = letra[i]
                posicion_reemplazo = random.randint(0, 99)
                letra[i] = letra[posicion_reemplazo]
                letra[posicion_reemplazo] = num
        return letra

#Leo el dataset de letras b
letras_b = pd.read_csv("data/letras_b.csv", sep=";", header=None)

#Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
letras_b = letras_b.to_numpy()

min_distorsion = 0.01
max_distorsion = 0.3
distorsionador = Distorsionador(min_distorsion, max_distorsion)

distorsionador.distorsionar(letras_b)


interfaz = Interfaz("900x700", 600, 600)
""" for i in range(10):
    interfaz.mostrar(letras_b[i], distorsiones[i])  """

#Guardo las letras distorsionadas en otro dataset llamado letras_b_dist
#Hay que manejar lo de que el 10% del dataset tiene que mantenerse original y no distorsionado


df_dist = pd.DataFrame(letras_b)
df_dist.to_csv("data/letras_b_dist.csv", sep=";", index=None, header=None)