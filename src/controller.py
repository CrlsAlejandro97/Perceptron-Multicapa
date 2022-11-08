from data_functions import generar_data_letras, distorsionar_letras, get_letras
from Perceptron import Perceptron

class Controller:

    def __init__(self, view):
        self.view = view

        # setting actions of view buttons
        view.set_command("generate", self.generar_data)
        view.set_command("create_perceptron", self.create_perceptron)
        view.set_command("train", self.train)


    def generar_data(self):
        cantidad = str(self.view.opcion_generar.get())
        print(cantidad)
        generar_data_letras(cantidad)
        distorsionar_letras(cantidad)
        self.view.create_label("Dataset generado!", row=2, column=2, columnspan=10)
    

    def train(self):
        cantidad = str(self.view.opcion_entrenar.get())
        letras = get_letras(cantidad)
        data_train = letras[:int(len(letras)*0.8)]
        data_test = letras[int(len(letras)*0.8)+1:int(len(letras)*0.8)+int(len(letras)*0.15)]
        data_validation = letras[int(len(letras)*0.8)+int(len(letras)*0.15)+1:99]
        print(self.perceptron.w[0][0][0])
        self.perceptron.train(data_train)
        print(self.perceptron.w[0][0][0])
            

    def create_perceptron(self):
        tamaño = self.view.entries["tamaño"].get()
        tamaño = tamaño.split(",")
        for t in range(len(tamaño)):
            tamaño[t] = int(tamaño[t])
        aprendizaje = float(self.view.scales["aprendizaje"].get())
        momento = float(self.view.scales["momento"].get())
        print(aprendizaje)
        print(momento)
        perceptron = Perceptron(tamaño, aprendizaje, momento)
        w, b = perceptron.init_params()
        capas = perceptron.init_layers()
        self.perceptron = perceptron

    # reading csv files
    """ def read(self):
        try:
            path = self.view.entries["trainpath"].get()
            with open(path) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_trainset(list(reader))

                # Conversion of number type columns to float
                for train in self.model.trainset:
                    self.model.add_class(train[-1])
                    for i in range(len(train) - 1):
                        train[i] = float(train[i])

                # Set colors based on class name
                self.model.set_train_colors([encode(row[-1]) for row in self.model.trainset])
                
            path = self.view.entries["testpath"].get()
            with open(path) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_testset(list(reader))

                # Conversion of number type columns to float
                for test in self.model.testset:
                    self.model.get_category_by_name(test[-1]).increase_size()
                    for i in range(len(test) - 1):
                        test[i] = float(test[i])

                # Set colors based on class name
                self.model.set_test_colors([encode(row[-1]) for row in self.model.testset])

            # Set dimensions of data in model 
            self.model.set_dimensions()
            # UI feedback
            self.view.get_entry("trainpath").config({"background": "pale green"})
            self.view.get_entry("testpath").config({"background": "pale green"})
            self.view.set_button_normal("train")
        except FileNotFoundError:
            # UI feedback
            self.view.get_entry("trainpath").config({"background": "tomato"})
            self.view.get_entry("testpath").config({"background": "tomato"}) """
