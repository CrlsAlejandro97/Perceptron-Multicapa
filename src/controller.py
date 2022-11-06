from data_functions import generar_data_letras, distorsionar_letras, get_letras
from Perceptron import Perceptron

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
        generar_data_letras(cantidad)
        distorsionar_letras(cantidad)
        self.view.create_label("Dataset generado!", row=2, column=2, columnspan=10)
    

    def train(self):
        cantidad = str(self.view.opcion_entrenar.get())
        letras = get_letras(cantidad)
        data_train = letras[:int(len(letras)*0.8)]
        data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
        data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]
        self.perceptron.train(data_train)
        
    def create_perceptron(self):
        neuronas_capa_1 = int(self.view.entries["neuronas_capa_1"].get())
        neuronas_capa_2 = int(self.view.entries["neuronas_capa_2"].get())
        tamaño = [neuronas_capa_1, neuronas_capa_2]
        aprendizaje = float(self.view.scales["aprendizaje"].get())
        momento = float(self.view.scales["momento"].get())
        print(aprendizaje)
        print(momento)
        perceptron = Perceptron(tamaño, aprendizaje, momento)
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
        
        
    