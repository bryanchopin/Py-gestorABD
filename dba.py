from ast import Str
import os, sys, time

parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD"


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'clear'
    os.system(command)

def createDirectorie():
    try:
        directory = input("Enter de dirName: ")
        parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    except OSError:
        print("Directorie created fail")
    else:
        print("Directorie created successfully")


def deleteDirectory():
    try:
        directory = input('Ingresa el directorio: ')
        path = os.path.join(parent_dir, directory)
        os.rmdir(path)
    except OSError:
        print("Directorie removed fail")
    else:
        print("Directorie removed successfully")

def deleteFile():
    # File name
    file = input('Ingresa el archivo y la extensión: ')
    # File location
    location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
    # Path
    path = os.path.join(location, file)
    # Remove the file
    # 'file.txt'
    os.remove(path)


def createFolder():
    print("Folder created successfully")

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
            cmd = str(input("Introduce comando: "))
            correcto = True
        except ValueError:
            print('Error, introduce un comando valido')
    return cmd






def menu():
    salir = False
    opcion = ["path base","ch","cha","exit,ls,mkdir,rmdir"]

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
        elif opcion == "rmdir":
            deleteDirectory()
        elif opcion == "mkdir":
            createDirectorie()
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