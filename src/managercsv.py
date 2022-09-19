from csv import reader
from random import random,randint

def readcsv(file):
    aux=[]
    # skip the first line(the header)
    with open(file, 'r') as my_file:
     file_csv = reader(my_file)
     head = next(file_csv)
      # check if the file is empty or not
     if head is not None:
        # Iterate over each row
        for i in file_csv:
            #save the rows
            aux.append(i)
        out=[]
        #Traverse array level
        for i in aux:
            #Traverse string level
            for j in i:
                word=j.replace(';','')
                out.append(word)
    return out

def blur(pattern,percetange):
    """Posiciones que se van difuminar segun el porcentaje: percentange"""
    position = sorted([randint(0,99) for i in range(int(percetange))])
    print(len(pattern))
    for i in range(int(10)):
        for j in range (int(10)):
            pass