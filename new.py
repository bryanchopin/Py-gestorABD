
from ast import Str
import os, sys, time

# # text = str(input('INGRESA UNA FRASE: '))



# def createFile():
#     try:
#         archivo = []
#         archivo.append(input('enter a words: ').split(','))
#         parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD"
#         for item in archivo:
#             open(f'/{parent_dir}/{item}.txt', "w")
#         # file.write("Primera línea" + os.linesep)
#         # file.write("Segunda línea")
#             item.close()
#     except OSError:
#             print ("File alredy exist")

#     # if archivo in os.listdir(parent_dir):
#     #     print ("File created fail")
#     # else:
#     #     print ("File created successfully")


# createFile()


# CREACION DE LISTAS A PARTIR DE LA FUNCION
# palabras = (input('enter a words: ').split(','))
# archivo = list(palabras)
# print(*archivo)



# def createFile():
#     try:
#         files = input("Enter de FileName: ").split(',')
#         archivo = list(files)
#         parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/"
#         for item in archivo:
#             file = open(f'/{parent_dir}/{item}.txt', "w")
#             # file.write("Primera línea" + os.linesep)
#             # file.write("Segunda línea")
#             file.close()
#             if archivo in os.listdir(parent_dir):
#                 print ("File created fail")
#             else:
#                 print ("File created successfully")
#     except OSError:
#             print ("File alredy exist")
            
            
# createFile()
parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/"

def createFile():
    files = input("Enter de FileName: ").split(',')
    archivo = list(files)
    parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/"
    for item in archivo:
        file = open(f'/{parent_dir}/{item}.txt', "w")
                # file.write("Primera línea" + os.linesep)
                # file.write("Segunda línea")
        file.close()
        if item not in archivo:
            print('file created successfully')
        elif item in archivo:
            print('file created failed')



def deleteFile():
    try:
        files = input("Enter de FileName: ").split(',')
        archivo = list(files)
        for item in archivo:
            path = os.path.join(parent_dir, item)
            os.remove(path)
    except OSError:
        print("File deleted fail")
    else:
        print("File deleted successfully")
        
createFile()