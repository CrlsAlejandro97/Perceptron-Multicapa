import pandas as pd
import numpy as np
import random

def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras

letras_100 = leer_letras(f"data/distorsionadas/100/letras.csv")

cant_neuronas_entrada = len(letras_100)
cant_neuronas_primera_capa = 5
cant_neuronas_segunda_capa = 5
cant_neuronas_salida = 3
cant_pesos = cant_neuronas_entrada*cant_neuronas_primera_capa + cant_neuronas_primera_capa*cant_neuronas_segunda_capa + cant_neuronas_segunda_capa*cant_neuronas_salida

w = []
for i in range(cant_pesos):
    w.append(random.random())



w1 = w[:500]
w2 = w[500:525]
w3 = w[525:540]
print(len(w1), len(w2), len(w3))

pesos = np

entrada_primera_capa_primera_neurona = w1[:]
#datos_entrada = letras_b_100[0]
#cant_neuronas_entrada = len(letras_b_100[0])
datos_salida = ["b", "d", "f"]
#cant_neuronas_salida = len(datos_salida)
print(500 + 25 + 15)
pesos = random.random()

