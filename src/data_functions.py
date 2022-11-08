import os
from random import shuffle
import numpy as np
import pandas as pd
import csv
from Distorsionador import Distorsionador

def get_letras_distorsionadas(cant):
    letras = (pd.read_csv(os.path.join(os.path.abspath(''),"src","data","distorsionadas",cant,'letras.csv'),sep=';',header=None)).to_numpy()
    return letras

def get_letras_originales(cant):
    letras = (pd.read_csv(os.path.join(os.path.abspath(''),"src","data","originales",cant,'letras.csv'),sep=';',header=None)).to_numpy()
    return letras
    

def generar_data_distorsionadas(cant):
    letras = get_letras_originales(cant)

    min_distorsion = 0.01
    max_distorsion = 0.3
    distorsionador = Distorsionador(min_distorsion, max_distorsion)
    
    letras_dist = distorsionador.distorsionar(letras)
    dataframe_dist_data = pd.DataFrame(letras_dist)

    dataframe_dist_data.to_csv(f"src/data/distorsionadas/{cant}/letras.csv", sep=";", index=None, header=None)

def generar_letra(letra):

    if letra == "B":
        letra_codigo = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    elif letra == "D":
        letra_codigo = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    else:
        letra_codigo = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    letra_codigo = np.reshape(letra_codigo, (1, 100))[0]
    return letra_codigo


def generar_data_letras(cant):

    letras = {
        "B": generar_letra("B"),
        "D": generar_letra("D"),
        "F": generar_letra("F")
    }
    
    tipo_letra = "B"
    c_letras = {
        'B': np.array([1, 0, 0]),
        'D': np.array([0, 1, 0]),
        'F': np.array([0, 0, 1])
    }
    letras_format_csv = []
    for i in range(int(cant)):
        if tipo_letra == "B":
            letras_format_csv.append(np.concatenate((letras["B"], c_letras["B"])))
            tipo_letra = "D"
        elif tipo_letra == "D":
            letras_format_csv.append(np.concatenate((letras["D"], c_letras["D"])))
            tipo_letra = "F"
        else:
            letras_format_csv.append(np.concatenate((letras["F"], c_letras["F"])))
            tipo_letra = "B"

    #Mezclo el dataset para mas aleatoriedad
    shuffle(letras_format_csv)
    
    file = open(f'src/data/originales/{str(cant)}/letras.csv', 'w+', newline ='')
    with file:   
        write = csv.writer(file, delimiter=';')
        write.writerows(letras_format_csv)
    file.close()