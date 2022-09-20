from Distorsionador import Distorsionador
from Interfaz import Interfaz
import pandas as pd
import numpy as np


def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras



def mostrar_letras(letras, distorsiones):
    interfaz = Interfaz("900x700", 600, 600)
    for i in range(98, 120):
        interfaz.mostrar(letras[i], distorsiones[i]) 


def main():
    min_distorsion = 0.01
    max_distorsion = 0.3
    distorsionador = Distorsionador(min_distorsion, max_distorsion)
    cantidades = ["100", "500", "1000"]
    letras = ["b", "d", "f"]
    for cant in cantidades:
        for letra in letras:
            #Leo la entrada
            data = leer_letras(f"data/originales/{cant}/letras_{letra}.csv")
            #Manipulo el dato
            distorsionador.distorsionar(data)
            dataframe_dist_data = pd.DataFrame(data)
    
            dataframe_dist_data.to_csv(f"data/distorsionadas/{cant}/letras_{letra}_dist.csv", sep=";", index=None, header=None)

main()


""" min_distorsion = 0.01
max_distorsion = 0.3
distorsionador = Distorsionador(min_distorsion, max_distorsion)
letras_b_100 = leer_letras("data/originales/100/letras_b.csv")
letras_d_100 = leer_letras("data/originales/100/letras_d.csv")
letras_f_100 = leer_letras("data/originales/100/letras_f.csv")

letras_b_500 = leer_letras("data/originales/500/letras_b.csv")
letras_d_500 = leer_letras("data/originales/500/letras_d.csv")
letras_f_500 = leer_letras("data/originales/500/letras_f.csv")

letras_b_1000 = leer_letras("data/originales/1000/letras_b.csv")
letras_d_1000 = leer_letras("data/originales/1000/letras_d.csv")
letras_f_1000 = leer_letras("data/originales/1000/letras_f.csv")


dist_letras_b_100 = distorsionador.distorsionar(letras_b_100)
dist_letras_d_100 = distorsionador.distorsionar(letras_d_100)
dist_letras_f_100 = distorsionador.distorsionar(letras_f_100)

dist_letras_b_500 = distorsionador.distorsionar(letras_b_500)
dist_letras_d_500 = distorsionador.distorsionar(letras_d_500)
dist_letras_f_500 = distorsionador.distorsionar(letras_f_500)

dist_letras_b_1000 = distorsionador.distorsionar(letras_b_1000)
dist_letras_d_1000 = distorsionador.distorsionar(letras_d_1000)
dist_letras_f_1000 = distorsionador.distorsionar(letras_f_1000)


mostrar_letras(letras_b_1000, dist_letras_b_1000)

#Guardo las letras distorsionadas en otro dataset llamado letras_b_dist """


