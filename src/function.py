import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def lineal(x):
    return x*0.1

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)


def adjustment_weight(w,x,alfa,err):
 #w: vector de pesos
 #x: vector de entrada
 #alfa: factor de aprendizaje
 #err: error de prediccion
 return w+(0.5*x*alfa*err)
