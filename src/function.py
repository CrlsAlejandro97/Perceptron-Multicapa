import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def lineal(x):
    return 0.1*x

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal():
    return 0.1 

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

def deltaHidden(W,deltaInput):
    #a no se usa porque f.activacion es lineal
    DELTA = []
    DELTA.append(deltaInput)
    for layer in reversed(W):
        wl = np.transpose(layer)
        delta=[]
        for i in range(len(wl)):
            delta.append(np.sum(wl[i]*deltaInput)*derivate_lineal())
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
    deltaOut = deltaHidden(W,deltaOut)
    #Ordenamos delta de inicio a fin
    deltaOut = deltaOut[::-1]
    return deltaOut

def Gradientdescent(deltas,W,Want,alfa,beta,):
    i=0
    Wres = []
    #Calculo para nuevos pesos
    for w, want in zip(W, Want):
        waux = []
        wl = np.transpose(w)
        wlant = np.transpose(want)
        for j in range(len(wl)):
           waux.append(np.array(wl[j]))
           wl[j] = wl[j] + deltas[i]*alfa + beta*(wl[j] - wlant[j])
        i=i+1
        Wres.append(np.array(waux))
    Want = Wres
    return Want, W



    
    




     



