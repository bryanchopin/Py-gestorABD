from ast import Str
import os, sys, time

parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD"


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'clear'
    os.system(command)



# UPDATED
# find new issue, incorrect evaluation in if
def createFile():
    files = input("Enter de FileName: ").split(',')
    archivo = list(files)
    for item in archivo:
        file = open(f'/{parent_dir}/{item}.txt', "w")
                # file.write("Primera línea" + os.linesep)
                # file.write("Segunda línea")
        file.close()
        if item not in archivo:
            print(f'file {item} created successfully')
        elif item in archivo:
            print('file created failed')



def createDirectorie():
    try:
        directory = input("Crea base ")
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    except OSError:
        print("DB created fail")
    else:
        print("DB created successfully")


# find new issue, failed deleting paths with roots
def deleteDirectory():
    try:
        directory = input('Borra base ')
        path = os.path.join(parent_dir, directory)
        os.rmdir(path)
    except OSError:
        print("DB removed fail")
    else:
        print("DB removed successfully")


# UPDATED
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

def changeDirectorie():
    os.chdir('../')
    print("Directorie changed successfully")

def listDir():
    dir_list = os.listdir(parent_dir)
    print("Files and directories in '", parent_dir, "' :") 
    print(dir_list)

def changeDirectorieA():
    os.chdir('..')
    print("Directorie changed successfully")

def currentPath():
    cP = os.getcwd()
    print("Current directorie:", cP)

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
    opcion = ["path base","ch","cha","exit","ls","crea base","borra base","create","rmcreate","clear"]

    while not salir:

        opcion = pedirComando()

        if opcion == "path base":
            currentPath()
        elif opcion == "ch":
            changeDirectorie()
        elif opcion == "cha":
            changeDirectorieA()
        elif opcion == "ls":
            listDir()
        elif opcion == "borra base":
            deleteDirectory()
        elif opcion == "crea base":
            createDirectorie()
        elif opcion == "create":
            createFile()
        elif opcion == "rmcreate":
            deleteFile()
        elif opcion == "clear":
            clearConsole()
        elif opcion == "exit":
            salir = True
        else:
            print ("Introduce un comando valido")

    print ("Fin")

def init():
    menu()

def layoutBrychxpin():
    print("----------------------------------------------------------")
    init()


layoutBrychxpin()