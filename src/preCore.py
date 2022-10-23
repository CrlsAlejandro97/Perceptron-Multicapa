import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from function import lineal, sigmoide
import os 


#Capa de entrada

ce = []

#Capa de salida

cs = []

#Primera capa oculta

c1 = []

#Segunda capa oculta

c2 = []

#Inicializamos los pesos (100 por cada neurona, tenemos 5 neuronas)

#Cantidades de neuronas por cada capa

cant_ce = 100
cant_cs = 3
cant_c1 = 5
cant_c2 = 5

#Cantidades de pesos

cant_pesos = cant_ce*cant_c1 + cant_c1*cant_c2 + cant_c2*cant_cs


#Codificacion de como se va a representar la salida de cada letra

y = {
    'b': [1, 0, 0],
    'd': [0, 1, 0],
    'f': [0, 0, 1]
}

#Generamos los pesos

#Total de valores de los pesos
w = np.random.rand(500)

#Valores de pesos en la primera capa, se separa por cada entrada de neurona
#Por ejemplo w11 son todos los pesos que van a impactar en la primera neurona de la primera capa

w11 = w[:100]
w12 = w[100:200]
w13 = w[200:300]
w14 = w[300:400]
w15 = w[400:500]

#Se genera una matriz de pesos para la primera capa, entonce si se pone W1[0][0] estariamos accediendo al primer peso
#que impacta en la primera neurona
W1 = [w11,w12,w13,w14,w15]

#Valores de pesos para la segunda capa
w = np.random.rand(25)
w21 = w[:5]
w22 = w[5:10]
w23 = w[10:15]
w24 = w[15:20]
w25 = w[20:25]
W2 = [w21,w22,w23,w24,w25]

#Valores de pesos para la capa de salida
w = np.random.rand(15)
w31 = w[:5]
w32 = w[5:10]
w33 = w[10:15]
W3 = [w31,w32,w33]

#Bias
B = random.random()


#Leer letras distorsionadas

letras_100 = pd.read_csv(os.path.join(os.path.abspath(''),"data","distorsiondas",'100','letras.csv'),sep=';',header=None).to_numpy()
letras_500 = pd.read_csv(os.path.join(os.path.abspath(''),"data","originales",'100','letras_d.csv'),sep=';',header=None).to_numpy()
letras_1000 = (pd.read_csv(os.path.join(os.path.abspath(''),"data","originales",'100','letras_f.csv'),sep=';',header=None)).to_numpy()[0]