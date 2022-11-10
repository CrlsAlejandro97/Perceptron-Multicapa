import numpy as np
import functionsMaths as f
import data_functions as df
import matplotlib.pyplot as plt

class Perceptron(object):

    def __init__(self, sizes, aprendizaje, momento, epocas):
        #
        
        self.sizes = sizes
        self.aprendizaje = aprendizaje
        self.momento = momento
        self.cant_capas = len(sizes) + 2
        self.epocas = epocas
    
    def init_params(self):
        w = []
        b = []
        w1 = np.random.rand(self.sizes[0], 100)
        b1 = np.random.rand(1, self.sizes[0])[0]

        [5, 5]
        
        if len(self.sizes) == 2:

            w2 = np.random.rand(self.sizes[1], self.sizes[0])
            w3 = np.random.rand(3, self.sizes[1])
            b2 = np.random.rand(1, self.sizes[1])[0]
            b3 = np.random.rand(1, 3)[0]
            w.append(w1)
            w.append(w2)
            w.append(w3)
            b.append(b1)
            b.append(b2)
            b.append(b3)


        elif len(self.sizes) == 1:
            w2 = np.random.rand(3, self.sizes[0])
            b2 = np.random.rand(1, 3)[0]
            w.append(w1)
            w.append(w2)
            b.append(b1)
            b.append(b2)

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

    def feedforward(self, x, w, b):
        cant_capas = self.cant_capas #4
        z = [x]
        y = [x] 
        for i in range(cant_capas-1):
            #0 ,1, 2
            yi = []
            zi = []
            for j in range(len(w[i])):
                #Suma ponderada
                entrada = np.dot(y[i],w[i][j])
                #Funcion de activacion
                if i == cant_capas - 2:
                    salida = f.sigmoide(entrada+b[i][j])
                else:
                    salida = f.lineal(entrada+b[i][j])
                zi.append(entrada)
                yi.append(salida)
            y.append(np.array(yi))
            z.append(np.array(zi))
         
        return y


    def backpropagation(self, ye, ys3, w):
        #ye: salida espera
        #ys3: salida obtenida
        #W:  vector peso de las capas

        #Delta de capa de salida
        deltaOut = f.derivate_error(ys3,ye)*f.derivate_sigmoide(ys3)
        deltas =[]
        deltas.append(deltaOut)
        i=0
        for wi in reversed(w):
            delta = np.dot(np.transpose(wi),deltas[i])*f.derivate_lineal()
            deltas.append(delta)
            i=i+1
        
        deltas = deltas[::-1]
        return deltas
        

    def gradiente_descendente(self, w, b, deltas, y, lr, m):
        #deltas 
        delta_w = [np.zeros(w.shape) for w in w]
        w_ant = w

        #ACTUALIZACION PESOS

        for i in range(len(w)):
            for j in range(len(w[i])):
                if i > 0:
                    for k in range(len(w[i-1])):

                        delta_w[i][j][k] = y[i][k]*deltas[i][j]*lr
                        w[i][j][k] = w[i][j][k] - delta_w[i][j][k]
                        w[i][j][k] += m*(w_ant[i][j][k] - w[i][j][k])
                else:
                    for k in range(100):

                        delta_w[i][j][k] = y[i][k]*deltas[i][j]*lr
                        w[i][j][k] = w[i][j][k] - delta_w[i][j][k]
                        w[i][j][k] += m*(w_ant[i][j][k] - w[i][j][k]) 

        #ACTUALIZACION BIAS
        #len(b) = 1
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j]-=deltas[i][j]*lr        

        return w, b
            

    def train(self, data_train):
        #Dividiendo data train en una tupla (entrada,clase)
        er = np.array([0,0,0])
        letras_train = []
        for letra in data_train:
            x_train = letra[:100]
            y_train = letra[100:]
            letras_train.append((x_train, y_train))

        w = self.w
        b = self.b
        err = []
  
        for e in range(self.epocas):
            np.random.shuffle(letras_train)
            for i in range(len(letras_train)):

                
                #Con feedforward obtengo la salida de todas las capas
                y = self.feedforward(letras_train[i][0], w, b)
                #!!-----Calculo del error-----!!!
                
                #La salida obtenida
                y_obtenido = y[-1]

                #La salida esperada
                ye = np.array(letras_train[i][1])

                #La sumatoria de errores

                er = np.sum([er, (ye-y_obtenido)**2], axis=0)
                #----------------------------------------------------#

                
                deltas = self.backpropagation(ye, y[-1], w[1:])

                

                #Backforward
                #w_prueba = w.copy()

                #Gradiente descendiete: Le paso los pesos, los deltas y las salidas de las capas
                
                w, b = self.gradiente_descendente(w, b, deltas, y[:3], self.aprendizaje, self.momento)
                
                        
                

            er = er/(2*len(letras_train))
            
            err.append(np.mean(er))

        for i in range(len(er)):
            er[i] = round(er[i]*100, 2)

        self.err = err

        self.w = w
        self.b = b
    

    def predecir(self, letra):
        cant_capas = self.cant_capas #4
        w = self.w
        b = self.b
        z = [letra]
        y = [letra] 
        for i in range(cant_capas-1):
            #0 ,1, 2
            yi = []
            zi = []
            for j in range(len(w[i])):
                #Suma ponderada
                entrada = np.dot(y[i],w[i][j])
                #Funcion de activacion
                if i == cant_capas - 2:
                    salida = f.sigmoide(entrada+b[i][j])
                else:
                    salida = f.lineal(entrada+b[i][j])
                zi.append(entrada)
                yi.append(salida)
            y.append(np.array(yi))
            z.append(np.array(zi))
        
        
        letras_predicciones = {}

        
        letras_predicciones["B"] = round(y[-1][0]*100,2)
        letras_predicciones["D"] = round(y[-1][1]*100,2)
        letras_predicciones["F"] = round(y[-1][2]*100,2)
                
        sorted_letras = dict(sorted(letras_predicciones.items(), key=lambda item:item[1], 
        reverse=True))
        
        #clase_salida = f.one_hot_encoding(y[-1])
        return sorted_letras
        
    def test_train(self, test):
        
        letras_test = []
        for letra in test:
            x_train = letra[:100]
            y_train = letra[100:]
            letras_test.append((x_train, y_train))

        letra = ["b","d","f"]
        porcentaje = 0
        for i in range(len(test)):
            y = self.feedforward(letras_test[i][0], self.w, self.b)
            salida = np.zeros_like(y[-1])
            salida = y[-1]
            if(np.argmax(salida) == np.argmax(letras_test[i][1])):
                porcentaje += 1
                print("Prediccion: {} letra: {} ---- valor real: {}, letra: {}".format( np.argmax(salida)+1,letra[ np.argmax(salida)],np.argmax(letras_test[i][1])+1,letra[np.argmax(letras_test[i][1])] ))
        print("Porcentaje predicho: {}%".format((porcentaje/len(test))*100))    






""" cantidad = "100"
letras = df.get_letras_distorsionadas(cantidad)
data_train = letras[:int(len(letras)*0.8)]
data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]


perceptron = Perceptron([5,5], 0.25, 0.2)
w, b = perceptron.init_params()
capas = perceptron.init_layers()

perceptron.train(data_train)

perceptron.test_train(data_test) """

