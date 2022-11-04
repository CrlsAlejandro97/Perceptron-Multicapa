import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def lineal(x):
    return x

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal():
    return 1 

def derivate_error(ye,ys):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return -(ye-ys)

#------------------------------
"""def feedFoward(X,W,B,layers):
    Y=[]
    #Capas Ocultas
    for i in range(len(layers)):
        y=[] #el problema es que la primera es y=X
        for j in range(len(W)-1):
            #Suma ponderada
            Z = np.dot(y,W[j])
            #Funcion de Activacion
            y.append(lineal(Z+B[j]))
        Y.append(np.array(y))"""

def deltaHidden(w,deltaInput):
    #a no se usa porque f.activacion es lineal
    DELTA = []
    DELTA.append(deltaInput)
    for layer in reversed(w):
        w = np.transpose(layer)
        delta=[]
        for i in range(len(w)):
            delta.append(np.sum(w[i]*deltaInput)*derivate_lineal())
        DELTA.append(delta)
        deltaInput =np.array(delta)
    
    return DELTA
    


def Backpropagation(ye,A,W):
    #Ye: es la salida espera
    #A: vector de salidas de activacion --> se podria eliminar y pasar solo la salida
    #W: pesos de las capas

    #Delta de capa de salida
    deltaOut = derivate_error(ye,A[len(A)-1])*derivate_sigmoide(A[len(A)-1])
    #Deltas de salida
    return deltaHidden(W,deltaOut)



    
    




     



