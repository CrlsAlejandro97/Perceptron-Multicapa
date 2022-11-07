import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1.0 / (1.0 + np.exp(-x))

def lineal(x):
    return 0.1*x

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal():
    return 0.1

def derivate_error(ys,ye):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return (ys-ye)


def one_hot_encoding(salida):
    clase = np.zeros_like(salida, dtype=int)
    #[0, 0, 0]

    #[0.87, 0.9, 0.7]
    #[0, 1, 0]
    clase[np.argmax(salida)] = 1

    return clase


