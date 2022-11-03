from random import shuffle
import numpy as np
import pandas as pd
import csv
from Distorsionador import Distorsionador

def get_letras(cant):
    letras = pd.read_csv(f"data/distorsionadas/{cant}/letras.csv",sep=';',header=None).to_numpy()
    return letras
    
def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras

def dataset_distorsion(dataset, cant):
    min_distorsion = 0.01
    max_distorsion = 0.3
    distorsionador = Distorsionador(min_distorsion, max_distorsion)
    
    distorsiones = distorsionador.distorsionar(dataset)
    dataframe_dist_data = pd.DataFrame(dataset)

    dataframe_dist_data.to_csv(f"data/distorsionadas/{cant}/letras.csv", sep=";", index=None, header=None)

    return distorsiones

def distorsionar_letras(cant):
    letras = leer_letras(f"data/originales/{cant}/letras.csv")
    #dataset_distorsion distorsiona las letras pasandole la cantidad de letras y las letras
    #devuelve las distorsiones de cada letra en una lista para asi no perder esa informacion
    #y guarda las letras distorsionadas en un archivo .csv
    distorsiones = dataset_distorsion(letras, cant)


def generar_letras():
    letra_b = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    letra_d = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


    letra_f = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    letras = {
        'b': letra_b,
        'd': letra_d,
        'f': letra_f
    }

    return letras

def generar_data_letras(cant):

    letras = generar_letras()
    "Recibe como parametro un diccionario de letras representadas en una matriz 10x10"
    letras["b"] = np.reshape(letras["b"], (1, 100))[0]
    letras["d"] = np.reshape(letras["d"], (1, 100))[0]
    letras["f"] = np.reshape(letras["f"], (1, 100))[0]
    
    tipo_letra = "b"
    c_letras = {
        'b': np.array([1, 0, 0]),
        'd': np.array([0, 1, 0]),
        'f': np.array([0, 0, 1])
    }
    letras_format_csv = []
    for i in range(int(cant)):
        if tipo_letra == "b":
            letras_format_csv.append(np.concatenate((letras["b"], c_letras["b"])))
            tipo_letra = "d"
        elif tipo_letra == "d":
            letras_format_csv.append(np.concatenate((letras["d"], c_letras["d"])))
            tipo_letra = "f"
        else:
            letras_format_csv.append(np.concatenate((letras["f"], c_letras["f"])))
            tipo_letra = "b"

    #Mezclo el dataset para mas aleatoriedad
    shuffle(letras_format_csv)
    
    file = open(f'data/originales/{str(cant)}/letras.csv', 'w+', newline ='')
    with file:   
        write = csv.writer(file, delimiter=';')
        write.writerows(letras_format_csv)
    file.close()