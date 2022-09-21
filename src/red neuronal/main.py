import pandas as pd
import numpy as np

def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras

letras_b_100 = leer_letras(f"data/distorsionadas/100/letras_b_dist.csv")
datos_entrada = letras_b_100[0]
cant_neuronas_entrada = len(letras_b_100[0])
datos_salida = ["b", "d", "f"]
cant_neuronas_salida = len(datos_salida)
