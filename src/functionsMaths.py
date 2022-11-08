import numpy as np

#Funciones de Activacion
def sigmoide(x):
    return 1.0 / (1.0 + np.exp(-x))

def lineal(x):
    return 0.1*x

#Derivadas
def derivate_sigmoide(x):
    return x*(1-x)

def derivate_lineal():
    return 0.1

def derivate_error(ys,ye):
    #ye es el valor esperado
    #ys es el valor calculado por la funcion de activacion
    return (ys-ye)


def one_hot_encoding(salida):
    clase = np.zeros_like(salida, dtype=int)
    #[0, 0, 0]

    #[0.87, 0.9, 0.7]
    #[0, 1, 0]
    clase[np.argmax(salida)] = 1

    return clase

def calculateDelta(ys,ye,W):
    #ye: salida espera
    #ys3: salida obtenida
    #W:  vector peso de las capas

    #Delta de capa de salida
    deltaOut = derivate_error(ys,ye)*derivate_sigmoide(ys)
    deltas =[]
    deltas.append(deltaOut)
    i=0
    for w in reversed(W):
      delta = np.dot(np.transpose(w),deltas[i])*derivate_lineal()
      deltas.append(delta)
      i=i+1
    return deltas[::-1]

def Gradientdescent_test(deltas,W,Want,activations,B,alfa,beta):
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



def gradiente_descendente(w,B, deltas, y, lr, m):
    #deltas 
    delta_w = [np.zeros(w.shape) for w in w]
    w_ant = w
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

    for j in range(len(B)):
        for k in range(len(B[j])):
            B[j][k]-=deltas[j][k]*lr         
                          
        return w,B


def feedforward(x, w, b):
        cant_capas = 4 #4
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
                    salida = sigmoide(entrada+b[i][j])
                else:
                    salida = lineal(entrada+b[i][j])
                zi.append(entrada)
                yi.append(salida)
            y.append(np.array(yi))
            z.append(np.array(zi))
         
        return y

#Calculo de MSE        
def get_mse(error,n):
    return error/(2*n)

def div_tuplas(data):
    letras = []
    for letra in data:
     x = letra[:100]
     y = letra[100:]
     letras.append((x, y))
    
    return letras


def init_params_test(layers):
        w = []
        b = []
        w1 = np.random.rand(layers[0], 100)
        b1 = np.random.rand(1, layers[0])[0]

        
        if len(layers) == 2:

            w2 = np.random.rand(layers[1], layers[0])
            w3 = np.random.rand(3, layers[1])
            b2 = np.random.rand(1, layers[1])[0]
            b3 = np.random.rand(1, 3)[0]
            w.append(w1)
            w.append(w2)
            w.append(w3)
            b.append(b1)
            b.append(b2)
            b.append(b3)


        elif len(layers) == 1:
            w2 = np.random.rand(3, layers[0])
            b2 = np.random.rand(1, 3)[0]
            w.append(w1)
            w.append(w2)
            b.append(b1)
            b.append(b2)

        w = w
        b = b
        return w, b