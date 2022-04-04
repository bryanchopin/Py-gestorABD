from ast import Str
import os, sys, time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'clear'
    os.system(command)

def createDirectorie():
    clearConsole()
    print("Directorie created successfully")
    layoutBrychxpin()

def createFolder():
    print("Folder created successfully")

def changeDirectorie():
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
    opcion = ["path","dos","tres","exit"]

    while not salir:

        opcion = pedirComando()

        if opcion == "path":
            currentPath()
        elif opcion == "dos":
            print ("Opcion 2")
        elif opcion == "tres":
            print("Opcion 3")
        elif opcion == "exit":
            salir = True
        else:
            print ("Introduce un comando valido")

    print ("Fin")






def init():
    # print("""
    # 1. Crear directorio
    # 2. Crear carpeta
    # 3. Mostar directorio actual
    # 4. cambiar de directorio
    # 5. Exit/Quit
    # """)
    menu()



def layoutBrychxpin():
    print(currentPath())
    print("-----------------------------------------------")
    init()


layoutBrychxpin()