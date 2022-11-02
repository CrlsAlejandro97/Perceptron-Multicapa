import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from functionsMaths import lineal, sigmoide
import os 


"""CONFIGURACION DE LOS DATOS"""

#Leer letras distorsionadas

letras_100 = pd.read_csv("data/distorsionadas/100/letras.csv",sep=';',header=None).to_numpy()
#letras_500 = pd.read_csv(os.path.join("data","distorsiondas",'100','letras.csv'),sep=';',header=None).to_numpy()
#letras_1000 = pd.read_csv(os.path.join("data","distorsiondas",'100','letras.csv'),sep=';',header=None).to_numpy()

#Dividir los datos de entrada en validacion, entrenamiento y test, en este caso primero para letras_100

letras_train_porc = 0.8
letras_test_porc = 0.15

cant_letras_train = int(len(letras_100)*letras_train_porc)
cant_letras_test = int(len(letras_100)*letras_test_porc)

letras_train = letras_100[:cant_letras_train]
letras_test = letras_100[cant_letras_train+1:cant_letras_train+cant_letras_test]
letras_validation = letras_100[cant_letras_train+cant_letras_test+1:]

# El set de validación se utilizará durante iteraciones que haremos con el conjunto de entrenamiento.


#Generar los conjuntos de entrenamiento, validacion y test

data_train = []
for letra in letras_train:
    x_train = letra[:100]
    y_train = letra[100:]
    data_train.append((x_train, y_train))


data_test = []
for letra in letras_test:
    x_test = letra[:100]
    y_test = letra[100:]
    data_train.append((x_test, y_test))

data_validation = []
for letra in letras_validation:
    x_validation = letra[:100]
    y_validation = letra[100:]
    data_validation.append((x_validation, y_validation))

"""CONFIGURACION DEL PERCEPTRON"""


cant_capas_ocultas = 2
coeficiente_aprendizaje = 0.4
momento = 0.7

#Cantidades de neuronas por cada capa

cant_ce = 100
cant_cs = 3
cant_c1 = 5
cant_c2 = 5

#Capa de entrada, se los inicializa en 0

ce = np.zeros(cant_ce, dtype=int)


#Capa de salida

cs = np.zeros(cant_cs, dtype=int)

cs = {}
for n in range(cant_cs):
    cs[n] = {
        "x": 0,
        "y": 0
    }

#Primera capa oculta

c1 = np.zeros(cant_c1, dtype=int)
c1 = {}
for n in range(cant_c1):
    c1[n] = {
        "x": 0,
        "y": 0
    }

#Segunda capa oculta

c2 = np.zeros(cant_c2, dtype=int)
c2 = {}
for n in range(cant_c2):
    c2[n] = {
        "x": 0,
        "y": 0
    }



#Inicializamos los pesos (100 por cada neurona, tenemos 5 neuronas)



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



for letra in data_train[:1]:
    x = letra[0]
    y = letra[1]
    ce = x[:]
    for i,n in enumerate(c1.keys()):
        entrada = np.dot(W1[i],x) + B
        c1[n]['x'] = entrada
        c1[n]['y'] = lineal(entrada)
    
    for i,n in enumerate(c2.keys()):
        c2[n]['x'] = np.dot(W2[i],c1[i]['y']) + B
        c2[n]['y'] = sigmoide(c2[n]['x'])
    
    salida = np.empty(3, dtype=float)
    for i,n in enumerate(cs.keys()):
        cs[n]['x'] = np.dot(W3[i],c2[i]['y']) + B
        cs[n]['y'] = sigmoide(cs[n]['x'])
        salida[i]= (cs[n]['y'])

    s = np.zeros_like(salida, dtype=int)
    s[salida.argmax(0)] = 1
    print(s)








