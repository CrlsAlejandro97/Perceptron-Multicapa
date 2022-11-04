import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1.0 / (1.0 + np.exp(-x))

def lineal(x):
    return 0.1*x

#Derivadas
def sigmoide_derivate(x):
    return sigmoide(x)*(1.0 - sigmoide(x))

def lineal_derivate():
    return 0.1

def cost_derivate(activation,y):
    return (activation - y)


