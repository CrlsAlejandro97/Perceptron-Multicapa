import numpy as np
import csv



def matriz_to_array(letras_matriz):
    "np.reshape me retorna la lista de 1x100 dentro de una lista, por eso eligo la posicion 0 para tener una lista plana"
    np.reshape(letras_matriz["b"], (1, 100))[0]
    np.reshape(letras_matriz["d"], (1, 100))[0]
    np.reshape(letras_matriz["f"], (1, 100))[0]
    return letras_matriz


def generar_data_originales(letras):
    "Recibe como parametro un diccionario de letras representadas en una matriz 10x10"
    letras["b"] = np.reshape(letras["b"], (1, 100))[0]
    letras["d"] = np.reshape(letras["d"], (1, 100))[0]
    letras["f"] = np.reshape(letras["f"], (1, 100))[0]
    
    cantidades = [100, 500, 1000]
    for cant in cantidades:
        tipo_letra = "b"
        c_letras = {
            'b': np.array([1, 0, 0]),
            'd': np.array([0, 1, 0]),
            'f': np.array([0, 0, 1])
        }
        letras_format_csv = []
        for i in range(cant):
            if tipo_letra == "b":
                letras_format_csv.append(np.concatenate((letras["b"], c_letras["b"])))
                tipo_letra = "d"
            elif tipo_letra == "d":
                letras_format_csv.append(np.concatenate((letras["d"], c_letras["d"])))
                tipo_letra = "f"
            else:
                letras_format_csv.append(np.concatenate((letras["f"], c_letras["f"])))
                tipo_letra = "b"

        file = open(f'data/originales/{str(cant)}/letras.csv', 'w+', newline ='')
        with file:   
            write = csv.writer(file, delimiter=';')
            write.writerows(letras_format_csv)
        file.close()



letra_b = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


letra_d = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


letra_f = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

letras = {
    'b': letra_b,
    'd': letra_d,
    'f': letra_f
}

""" letras["b"] = np.reshape(letras["b"], (1, 100))[0]

w = np.array([1, 0, 0])
con = np.concatenate((letras['b'], w))
print(letras['b'])
print(w)
print(con)

print(type(letras['b']))
print(type(w)) """

generar_data_originales(letras)