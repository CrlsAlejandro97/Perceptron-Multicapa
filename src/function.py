from math import exp

import numpy as np
def sigmoide(x):
    return 1/1+np.exp(-x)

def lineal(x):
    c=9.572340
    if x>c:
        return 1
    else:
        return 0
