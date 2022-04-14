
from ast import Str
import os, sys, time

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