
# text = str(input('INGRESA UNA FRASE: '))
# lista = []
# # palabras = lista.append(str(input('enter a words: ')))
# # str(lista).split(',')
# lista.append(text.split(','))


# for item in lista:
#     print(item)

from ast import Str
import os, sys, time

def createFile():

    try:
        list = (str(input('Enter de FileName: ').split(',')))
        # parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/"
        for item in list:
            # file = open(f'/{parent_dir}/{item}.txt', "w")
            # file.write("Primera línea" + os.linesep)
            # file.write("Segunda línea")
            # file.close()
            print(item)

        # if item in os.listdir(parent_dir):
        #     print ("File created successfully")

    except OSError:
        print ("File created fail")

createFile()
