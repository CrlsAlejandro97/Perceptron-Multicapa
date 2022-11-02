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

def error(ye,ys):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return ye-ys

def deltaHidden(w,a,deltaInput):
    


def Backpropagation(ye,A,W):
    #Ye: es la salida espera
    #A: vector de salidas de activacion
    #W: pesos de las capas
    ultOut = np.array(A[len(A)])
    deltaOut = []
    #Delta de la capa de salida
    for i in range(len(ultOut)):
        derivate_error =-error(ye[i],A[i])
        deltaOut.append(derivate_error*derivate_sigmoide(ultOut[j]))
    deltaOut = np.array(deltaOut)

    #Delta de capas ocultas


     



