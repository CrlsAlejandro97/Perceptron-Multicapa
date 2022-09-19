from Distorsionador import Distorsionador
from Interfaz import Interfaz
import pandas as pd
import numpy as np

#Guardo las distorsiones para ir mostrando cuanta distorsion tiene cada letra
#Ver como manejar mejor esto

def leer_letras(path):
    #Leo el dataset de letras b
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras

#letras_b = leer_letras("data/letras_b.csv")
letras_b = leer_letras("data/originales/100/letras_b.csv")
#letras_f = leer_letras("data/letras_b.csv")
min_distorsion = 0.01
max_distorsion = 0.3

distorsionador = Distorsionador(min_distorsion, max_distorsion)

distorsiones_letra_b = distorsionador.distorsionar(letras_b)

def mostrar_letras(letras, distorsiones):
    interfaz = Interfaz("900x700", 600, 600)
    for i in range(10, 20):
        interfaz.mostrar(letras[i], distorsiones[i]) 

mostrar_letras(letras_b, distorsiones_letra_b)

#Guardo las letras distorsionadas en otro dataset llamado letras_b_dist

""" df_dist = pd.DataFrame(letras_b)
df_dist.to_csv("data/letras_b_dist.csv", sep=";", index=None, header=None) """