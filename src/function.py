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

    




    
    




     



