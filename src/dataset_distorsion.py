from Distorsionador import Distorsionador
from Interfaz import Interfaz
import pandas as pd

def leer_letras(path):
    #Leo el dataset de letras
    letras = pd.read_csv(path, sep=";", header=None)

    #Lo convierto de dataFrame a un arreglo de numpy para manipularlo mejor
    letras = letras.to_numpy()

    return letras

def mostrar_letras(letras, distorsiones):
    interfaz = Interfaz("900x700", 600, 600)
    for i in range(10, 90):
        interfaz.mostrar(letras[i], distorsiones[i]) 

def dataset_distorsion(dataset, cant):
    min_distorsion = 0.01
    max_distorsion = 0.3
    distorsionador = Distorsionador(min_distorsion, max_distorsion)
    
    distorsiones = distorsionador.distorsionar(dataset)
    dataframe_dist_data = pd.DataFrame(dataset)

    dataframe_dist_data.to_csv(f"data/distorsionadas/{cant}/letras.csv", sep=";", index=None, header=None)

    return distorsiones

def main():
    cantidades = ["100", "500", "1000"] 
    for cant in cantidades:
        letras = leer_letras(f"data/originales/{cant}/letras.csv")
        #dataset_distorsion distorsiona las letras pasandole la cantidad de letras y las letras
        #devuelve las distorsiones de cada letra en una lista para asi no perder esa informacion
        #y guarda las letras distorsionadas en un archivo .csv
        distorsiones = dataset_distorsion(letras, cant)

main()

