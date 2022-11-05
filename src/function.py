import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def lineal(x):
    return x*0.1

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal():
    return 0.1 

def derivate_error(ys,ye):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return (ys-ye)


# def deltaHidden(W,deltaInput):
#     #a no se usa porque f.activacion es lineal
#     DELTA = []
#     DELTA.append(deltaInput)
#     for layer in reversed(W):
#         wl = np.transpose(layer)
#         delta=[]
#         for i in range(len(wl)):
#             delta.append(np.sum(wl[i]*deltaInput)*derivate_lineal())
#         DELTA.append(delta)
#         deltaInput =np.array(delta)
    
#     return DELTA
    


def calculateDelta(ye,ys3,W):
    #ye: salida espera
    #ys3: salida obtenida
    #W:  vector peso de las capas

    #Delta de capa de salida
    deltaOut = derivate_error(ys3,ye)*derivate_sigmoide(ys3)
    deltas =[]
    deltas.append(deltaOut)
    i=0
    for w in reversed(W):
      delta = np.dot(np.transpose(w),deltas[i])*derivate_lineal()
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
           new_weight.append(W[i][j] - alfa*deltas[i][j]*activations[i]) #+ beta*(W[i][j] - Want[i][j]))
        waux = np.array(waux)
        new_weight = np.array(new_weight)
        Wres.append(waux)
        Wnext.append(new_weight)
    
    return Wres,Wnext,B
    




    
    




     



