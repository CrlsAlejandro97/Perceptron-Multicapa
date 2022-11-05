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

def calculateDelta(ye,ys3,W):
    #ye: salida espera
    #ys3: salida obtenida
    #W:  vector peso de las capas

    #Delta de capa de salida
    deltaOut = cost_derivate(ys3,ye)*sigmoide_derivate(ys3)
    deltas =[]
    deltas.append(deltaOut)
    i=0
    for w in reversed(W):
      delta = np.dot(np.transpose(w),deltas[i])*lineal_derivate()
      deltas.append(delta)
      i=i+1
    return deltas[::-1]

def Gradientdescent(deltas,W,Want,activations,B,alfa,beta):
    #Pesos anteriores
    Wres = []
    #Pesos actualizados
    Wnext = []
    #Calculo para nuevos pesos
    for i in range(len(W)):
        waux = []
        new_weight = []
        #Actualizacion de bias
        B[i] = B[i] - alfa*deltas[i]
        #Actualizacion de pesos
        for j in range(len(W[i])):
           #Resguardo peso actual
           waux.append(W[i][j])
           #Peso actualizado
           new_weight.append(W[i][j] - alfa*deltas[i][j]*activations[i] + beta*(W[i][j] - Want[i][j]))
        waux = np.array(waux)
        new_weight = np.array(new_weight)
        Wres.append(waux)
        Wnext.append(new_weight)
    
    return Wres,Wnext,B
