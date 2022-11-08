import data_functions as df
from Perceptron import Perceptron
from Distorsionador import Distorsionador
import numpy as np
from tkinter import *
import customtkinter

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
        epocas = int(self.view.entries["epocas"].get())
        perceptron = Perceptron(sizes, aprendizaje, momento, epocas)
        w, b = perceptron.init_params()
        capas = perceptron.init_layers()
        print(momento)
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

        letra_prediccion, porc_prediccion = self.perceptron.predecir(letra_distorsionada)
        self.mostrarLetra(letra_distorsionada, letra_prediccion, porc_prediccion)
        #texto_prediccion = f"Prediccion: Letra {letra_prediccion} con un acierto del {porc_prediccion}%"
        #self.view.mostrarLetra(letra_distorsionada)
        
        

    
    def mostrarLetra(self, letra_distorsionada, letra_prediccion, porc):
        
        if self.view.frames["letraMatriz"].winfo_exists() == 1:
            self.view.frames["letraMatriz"].destroy()
        
        frame = self.view.createviewLetraMatriz()
        texto_prediccion = f"Prediccion: Letra {letra_prediccion} con un acierto del {porc}%"
        label_prediccion = customtkinter.CTkLabel(master=self.view.frames["letraMatriz"], text=texto_prediccion)
        label_prediccion.place(x=30, y=325)

        letra_2d = np.reshape(letra_distorsionada, (10,10))
        list_btn = []
        for i in range(10):
            list_btn.append([])
            for j in range(10):
                list_btn[i].append(customtkinter.CTkButton(frame, relief="solid", corner_radius=0, hover=False, text="", border_width =1, border_color="#FFFFFF"))
                list_btn[i][j].pack()
                if (letra_2d[i][j] ==1 ):
                    list_btn[i][j].configure(bg="blue", fg_color="black")
                list_btn[i][j].place(relx = 0.06 + 0.06*j, rely = 0.07 + 0.07*i, relwidth= 0.06, relheight=0.07) 
        

        
        
    