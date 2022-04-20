from ast import Str
from cmath import e
from ntpath import join
import os, sys, time,re

parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/DB/"

#UPDATED AND NEW FUNCTIONS


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'clear'
    os.system(command)
def helpConsole():
    print('''
    --COMMANDS
    HELP :
    CLEAR :
    EXIT:
    CREA BASE:
    BORRA BASE:
''')


def crearDB():
    try:
        directory = input("Crea base ")
        com = re.findall(";$",directory)
        if com:
            directory = directory.replace(";","")
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            print("DB created successfully")
        else:
            print('DB created fail')
    except OSError:
        print("DB created fail")

# find new issue, failed deleting paths with roots
def borrarDB():
    try:
        directory = input('Borra base ')
        com = re.findall(";$",directory)
        if com:
            directory = directory.replace(";","")
            path = os.path.join(parent_dir, directory)
            os.rmdir(path)
            print("DB removed successfully")
        else:
            print("DB removed fail")
    except OSError:
        print("DB removed fail")

def MuestraDB():
    dir_list = os.listdir(parent_dir)
    for item in dir_list:
        print(f"DB name: {item}")

def usaDB():
    try:
        DBname = input("Usa base ")
        com = re.findall(";$",DBname)
        if com:
            DBname = DBname.replace(";","")
            path = os.path.join(parent_dir,DBname)
            os.chdir(path)
            currentPath()
            print(f"DB selected {DBname}")
        else:
            print("DB moved fail")
    except OSError:
        print("DB created fail")





# UPDATED
# find new issue, incorrect evaluation in if
def createTable():
    try:
        files = input("Crea tabla ").split(',')
        archivo = list(files)
        path = os.getcwd()
        for item in archivo:
            dat = open(f'/{path}/{item}.dat', "w")
                    # file.write("Primera línea" + os.linesep)
                    # file.write("Segunda línea")
            dat.close()
            est = open(f'/{path}/{item}.est', "w")
                # file.write("Primera línea" + os.linesep)
                # file.write("Segunda línea")
            est.close()
            print(f'file {item} created successfully')
    except OSError:
        print("file created fail")

# UPDATED UPDATED
def deleteTable():
    try:
        files = input("Borra tabla ").split(',')
        archivo = list(files)
        ruta = os.getcwd()
        for item in archivo:
            path = os.path.join(ruta, item)
            os.remove(path)
            print(f"File {item} deleted successfully")
    except OSError:
        print("File deleted fail")













def currentPath():
    cP = os.getcwd()
    print(cP)


def changeDirectorieA():
    os.chdir('..')
    print("Directorie changed successfully")








def pedirComando():
    correcto = False
    while(not correcto):
        try:
            cmd = str(input("brychxpin: "))
            correcto = True
        except ValueError:
            print('Error, introduce un comando valido')
    return cmd

def menu():
    salir = False
    opcion = ["path base","usa base","exit","muestra bases;","crea base","borra base","crea tabla","borra tabla","clear","help"]

    while not salir:

        opcion = pedirComando()

        if opcion == "path base":
            currentPath()
        elif opcion == "usa base":
            usaDB()
        elif opcion == "muestra bases;":
            MuestraDB()
        elif opcion == "borra base":
            borrarDB()
        elif opcion == "crea base":
            crearDB()
        elif opcion == "crea tabla":
            createTable()
        elif opcion == "borra tabla":
            deleteTable()
        elif opcion == "clear":
            clearConsole()
        elif opcion == "help":
            helpConsole()
        elif opcion == "exit":
            salir = True
        else:
            print ("Introduce un comando valido")

    print ("Fin")

def init():
    menu()

def layoutBrychxpin():
    print("-----------------------------------------------------------")
    init()


layoutBrychxpin()