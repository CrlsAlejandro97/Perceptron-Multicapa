import numpy as np
import random

class Perceptron(object):
    def __init__(self, sizes, aprendizaje, momento):
        self.sizes = sizes
        self.aprendizaje = aprendizaje
        self.momento = momento
    
    def init_params(self):
        w = []
        b = []
        w.append(np.random.rand(self.sizes[0], 100))
        if len(self.sizes) > 1:
            w.append(np.random.rand(self.sizes[1], self.sizes[0]))
            w.append(np.random.rand(3, self.sizes[1]))
        else:
            w.append(np.random.rand(3, self.sizes[0]))
        
        self.w = w
        self.b = b
        return w, b
    
    def init_layers(self):
        capa_entrada = np.zeros(100, dtype=int)
        capa_salida = np.zeros(3, dtype=float)
        capas_ocultas = []

        for i in range(len(self.sizes)):
            capa_oculta = np.zeros(self.sizes[i])
            capas_ocultas.append(capa_oculta)
        
        capas = [capa_entrada, *capas_ocultas, capa_salida]
        self.capas = capas
        return capas
    
    def train(self, data_train):
        #Dividiendo data train en una tupla (entrada,clase)
        letras_train = []
        for letra in data_train:
            x_train = letra[:100]
            y_train = letra[100:]
            letras_train.append((x_train, y_train))

        w = self.w
        b = self.b

        

    def _divX_Y(letras):
        for letra in letras:
            x_train = letra[:100]
            y_train = letra[100:]
        return x_train,y_train

    

    
