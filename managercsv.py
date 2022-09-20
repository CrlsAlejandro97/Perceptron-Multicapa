from csv import reader
from random import random,randint
import pandas as pd

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
    position = sorted([randint(1,100) for i in range(int(percetange))])
    pattern=pd.DataFrame(pattern)
    print(pattern[0])
    """for i in range(1,10):
        for j in range (1,10):
            for z in position:
             if(k+j)==z:
                 if (pattern[i][j]=='0'):
                     pattern[i][j]=chr(1)
                 else:
                     pattern[i][j]=chr(0)"""


            
            

        


