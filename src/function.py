from math import exp

import numpy as np
def sigmoide(x):
    return 1/(1+np.exp(-x))

def lineal(x):
    return x*0.1

def adjustment_weight(w,x,alfa,err):
 #w: vector de pesos
 #x: vector de entrada
 #alfa: factor de aprendizaje
 #err: error de prediccion
 return w+0.5*x*alfa*err