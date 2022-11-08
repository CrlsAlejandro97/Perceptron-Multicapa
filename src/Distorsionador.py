import random
import math

class Distorsionador:
    def __init__(self, min_distorsion, max_distorsion):
        self.min_distorsion = min_distorsion
        self.max_distorsion = max_distorsion
    
    def _calcDistorsion(self):

        # Se calcula la distorsion que va a tener la letra en un rangon de min_distorsion a max_distorsion
        distorsion = round(random.uniform(self.min_distorsion, self.max_distorsion), 2)
        return distorsion
    
    def distorsionar(self, letras):
        # El 10% de las letras tienen que mantenerse originales
        cant_sin_dist = int(0.1 * len(letras))
        letras_dist = letras.copy()
        for i in range(len(letras)):
            #Arranco a distorsionar el dataset desde la posicion igual al 10% de la cantidad de letras que hay en el ds
            if i > int(cant_sin_dist):
                
                letra = letras[i]
                distorsion = self._calcDistorsion()
                
                letras_dist[i] = self._dist_letra(letra, distorsion)
            else:
                distorsion = 0
        
        
        return letras_dist

    def _dist_letra(self, letra, distorsion):
        
        # Recorro el arreglo de la letra y si hay un uno hay una probabilidad de un x porciento de que se cambie de lugar dependiendo de la distorsion calculada
        posiciones_uno = []
        posiciones_cero = []
        #Le resto 3 ya que solamente selecciono hasta la posicion 100, a partir de la 100 se encuentran datos asociados a que tipo de clase pertenece y no se lo debe distorsionar
        for i in range(len(letra)-3):
            if letra[i] == 1:
                posiciones_uno.append(i)
            else:
                posiciones_cero.append(i)

        celdas_mover = math.ceil(distorsion*len(posiciones_uno))

        while celdas_mover > 0:
            posicion_uno = random.choice(posiciones_uno)
            posicion_cero = random.choice(posiciones_cero)
            letra[posicion_cero] = 1
            letra[posicion_uno] = 0
            posiciones_cero.remove(posicion_cero)
            posiciones_uno.remove(posicion_uno)
            celdas_mover-=1
            
        return letra

    
    













