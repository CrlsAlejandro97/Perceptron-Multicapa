from Distorsionador import Distorsionador
from Interfaz import Interfaz
import pandas as pd
import numpy as np
import random
import math

def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=",", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras


def mostrar_letras(letras, distorsiones):
    interfaz = Interfaz("900x700", 600, 600)
    for i in range(10, 90):
        interfaz.mostrar(letras[i], distorsiones[i]) 

def generar_data_originales(cant):
    letra_b = leer_letras("data/letra_b.csv")
    letra_d = leer_letras("data/letra_d.csv")
    letra_f = leer_letras("data/letra_f.csv")
    letras = {
        'b': letra_b,
        'd': letra_d,
        'f': letra_f
    }
    cantidades = ["100", "500", "1000"]
    for cant in cantidades:
        pass

def main():
    min_distorsion = 0.01
    max_distorsion = 0.3
    distorsionador = Distorsionador(min_distorsion, max_distorsion)
    
    cantidades = ["100", "500", "1000"]
    for cant in cantidades:
        #Leo la entrada
        data = leer_letras(f"data/originales/{cant}/letras.csv")
        #Manipulo el dato
        distorsionador.distorsionar(data)
        dataframe_dist_data = pd.DataFrame(data)

        dataframe_dist_data.to_csv(f"data/distorsionadas/{cant}/letras.csv", sep=",", index=None, header=None)




main()


