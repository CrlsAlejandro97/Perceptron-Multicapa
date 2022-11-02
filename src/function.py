import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def lineal(x):
    return x

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal(x):
    return 1 

def derivate_error(ye,ys):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return -(ye-ys)

def deltaHidden(w,a,deltaInput):
    


# def Backpropagation(ye,A,W):
#     #Ye: es la salida espera
#     #A: vector de salidas de activacion
#     #W: pesos de las capas
#     #Delta de capas ocultas
#     deltaOut = derivate_error(ye,A[len(A)])*derivate_sigmoide(A[len(A)])
#     #Delta de la capa de salida
#     #Delta de capas ocultas


     



