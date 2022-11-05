import numpy as np
import functionsMaths as f

class Perceptron(object):
    def __init__(self, sizes, aprendizaje, momento):
        self.sizes = sizes
        self.aprendizaje = aprendizaje
        self.momento = momento
    
    def init_params(self):
        w = []
        b = []
        w1 = np.random.rand(self.sizes[0], 100)
        b1 = np.random.rand(1, self.sizes[0])[0]

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

    def feedforward(self, x, w, b, cant_capas):
        z = [x]
        y = [x] 
        #cant_capas = 4
        for i in range(cant_capas-1):
            yi = []
            zi = []
            for j in range(len(w[i])):
                #Suma ponderada
                """ print("i: ", str(i), "j: ", str(j))
                print("y[0]: " ,y[i]) """
                entrada = np.dot(y[i],w[i][j])
                #Funcion de activacion
                if i == cant_capas - 2:
                    salida = f.sigmoide(entrada+b[i][j])
                else:
                    salida = f.lineal(entrada+b[i][j])
                zi.append(entrada)
                yi.append(salida)
            y.append(np.array(yi))
            print()
            z.append(np.array(zi))
        
        print(len(y))
        
        print("Capa salida de la funcion: ", y[-1])
        return y[-1]



    def train(self, data_train):
        #Dividiendo data train en una tupla (entrada,clase)
        letras_train = []
        for letra in data_train:
            x_train = letra[:100]
            y_train = letra[100:]
            letras_train.append((x_train, y_train))

        w = self.w
        b = self.b
  
        for e in range(1):
            np.random.shuffle(letras_train)
            
            """ 
                for epoca 

                feedforward(x_train , w, b) ==> retorna la salida de la ultima capa
                backpropagation(y_train, salida_obtenida, w, b, capas) => retorna una lista de deltas para cada capa 
                gradiente_descent(delta, aprendizaje, momento, w, b) => retorna los pesos actualizados

                for i in range(len(w)):

            """
            for i in range(1):

                # feedforward
                cant_capas = len(self.sizes)+2
                #Primer capa oculta
                ys1 =[]
                z1 = []
                deltas = []
                zs = []
                activaciones = [letras_train[i][0]]
                for j in range(len(w[0])):
                    #Suma ponderada
                    Z1 = np.dot(letras_train[i][0],w[0][j])
                    #Funcion de activacion
                    ys1.append(f.lineal(Z1+b[0][j]))
                    z1.append(Z1)
                
                z1 = np.array(z1)
                ys1 = np.array(ys1)

                activaciones.append(ys1)
                zs.append(z1)
                #Segunda capa
                ys2 = []
                z2 = []
                for j in range(len(w[1])):
                    #Suma ponderada
                    Z2 = np.dot(ys1,w[1][j])
                    #Funcion de activacion
                    ys2.append(f.lineal(Z2+b[1][j]))
                    z2.append(Z2)
                
                z2 = np.array(z2)
                ys2 = np.array(ys2)
                
                activaciones.append(ys2)
                zs.append(z2)
                #Capa de salida
                ys3 = []
                z3 = []
                for j in range(len(w[2])):
                    #Suma ponderada
                    Z3 = np.dot(ys2,w[2][j])
                    #Funcion de activacion
                    ys3.append(f.sigmoide(Z3+b[2][j]))
                    z3.append(Z3)
                print("Capa salida: ", ys3)
                self.feedforward(letras_train[i][0], w, b, cant_capas)
                #!!-----Calculo del error-----!!!

                ys3 = np.array(ys3)
                z3 = np.array(z3)

                activaciones.append(ys3)
                zs.append(z3)

                Ye = np.array(letras_train[i][1])
                #----------------------------------------------------#

                delta = f.cost_derivate(activaciones[3], Ye)*f.sigmoide_derivate(z3)
                delta = np.array(delta)
                b[2] -= delta*0.3 

                deltas.append(delta)
                ##print(ys3, letras_train[i][1],delta)
                #CAPA OCULTA N° 2
                delta2 = np.dot(np.transpose(w[2]),deltas[0])*f.lineal_derivate()
                b[1] -= delta2*0.3

                deltas.append(delta2)

                #CAPA OCULTA N° 1
                delta1 = np.dot(np.transpose(w[1]),deltas[1])*f.lineal_derivate()
                b[0] -= delta1*0.3

                deltas.append(delta1)

                #Backforward
                for j in range(len(w[2])):
                    for k in range(len(w[1])):
                        w[2][j][k] -= activaciones[2][k]*deltas[0][j]*0.3
                
                for j in range(len(w[1])):
                    for k in range(len(w[0])):
                        w[1][j][k] -= activaciones[1][k]*deltas[1][j]*0.3

                for j in range(len(w[0])):
                    for k in range(100):
                        w[0][j][k] -= activaciones[0][k]*deltas[2][j]*0.3 

    def _divX_Y(letras):
        for letra in letras:
            x_train = letra[:100]
            y_train = letra[100:]
        return x_train,y_train

    


w3 = np.random.rand(3, 5)
delta = np.array([0.3, 0.05, 0.17])

""" print(w3)
print(np.transpose(w3)) """
print(np.dot(np.transpose(w3),delta)*f.lineal_derivate())