import data_functions as df
from Perceptron import Perceptron
from Distorsionador import Distorsionador
from Interfaz import Interfaz 

class Controller:

    def __init__(self, view):
        self.view = view

        # setting actions of view buttons
        view.set_command("generate", self.generar_data)
        view.set_command("create_perceptron", self.create_perceptron)
        view.set_command("train", self.train)
        view.set_command("predecir", self.predecir_letra)


    def generar_data(self):
        cantidad = str(self.view.opcion_generar.get())
        df.generar_data_letras(cantidad)
        df.generar_data_distorsionadas(cantidad)
        self.view.create_label("Dataset generado!", row=2, column=2, columnspan=10)
    

    def train(self):
        cantidad = str(self.view.opcion_entrenar.get())
        letras = df.get_letras_distorsionadas(cantidad)
        data_train = letras[:int(len(letras)*0.8)]
        data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
        data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]
        self.perceptron.train(data_train)
        
    def create_perceptron(self):
        neuronas_capa_1 = int(self.view.entries["neuronas_capa_1"].get())
        neuronas_capa_2 = int(self.view.entries["neuronas_capa_2"].get())
        if neuronas_capa_1 == 0:
            sizes = [neuronas_capa_2]
        elif neuronas_capa_2 == 0:
            sizes = [neuronas_capa_1]
        else:
            sizes = [neuronas_capa_1, neuronas_capa_2]
        aprendizaje = float(self.view.scales["aprendizaje"].get())
        momento = float(self.view.scales["momento"].get())
        perceptron = Perceptron(sizes, aprendizaje, momento)
        w, b = perceptron.init_params()
        capas = perceptron.init_layers()
        self.perceptron = perceptron

    def predecir_letra(self):
        opcion_letra = self.view.opcion_letra.get()
        if opcion_letra == 1:
            letra="B"
        elif opcion_letra == 2:
            letra="D"
        else:
            letra = "F"
        
        distorsion = float(self.view.scales["distorsion"].get())
        distorsionador = Distorsionador(0, 0.3)
        letra_codigo = df.generar_letra(letra)
        letra_distorsionada = distorsionador._dist_letra(letra_codigo, distorsion)

        letra_prediccion = self.perceptron.predecir(letra_distorsionada)
        print(letra_prediccion)

        interfaz = Interfaz("500x500", 500, 500)
        interfaz.mostrar(letra_distorsionada, distorsion)

        
        
    