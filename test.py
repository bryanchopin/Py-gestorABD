from ast import Str
from cmath import e
from dataclasses import field
from ntpath import join
import os, sys, time,re
import shutil,linecache


# parent_dir = "/Users/akisechopen/Desktop/UNIVERSIDAD/10 semestre/administracion de bases de datos/proyecto ABD/DB/"
cP = os.getcwd()
parent_dir = cP + "/DB"

#UPDATED AND NEW FUNCTIONS
class own:
    def __init__(self):
        self.campo = []
        self.tipos = ["caracter","entero","decimal","fecha"]
        self.Validartipo = False
        self.validarLongitud = False
        self.validarLenght = False
        self.validarUsebase = False
        self.fileExist = False
        self.addField = False

        self.validarFieldType = False
        self.validarFieldLen = False


    def nombreCampo(string):
        print("hi im fieldname")
        return

    def tipoCampo(tipo):
        print("hi im fielType")
        return

    def longitudCampo(string):
        print("hi im lenghtfield")
        return



obj = own()


def validarTabla(Atributos):
    try:
        #validando los espacios de la query
        if len(Atributos) == 3:
            obj.validarLenght = True

        #validando los tipos de campo
        for x in obj.tipos:
            if Atributos[1] == x:
                obj.Validartipo = True

        if Atributos[1] == obj.tipos[3]:
            obj.validarLenght = True
            obj.validarLongitud = True

        # validando si la longitud en un entero
        elif str.isdigit(Atributos[2]):
            obj.validarLongitud = True

        # validando si la longitud en un Float
        elif '.' in Atributos[2]:
            Atributos[2] = float(Atributos[2])
            obj.validarLongitud = True


        return
    except:
        print("Field error")

def tabla(file,path):

    try:
        Atributos = input("")
        com = re.findall(";$",str(Atributos))
        Atributos = Atributos.replace(";","")
        Latrib = Atributos.split(",")

        validarTabla(Latrib)

        if obj.validarLenght and obj.Validartipo and obj.validarLongitud:
            obj.campo.append(Latrib)
            if com:
                if obj.addField:
                    addWrite(file,path)
                    obj.Validartipo = False
                    obj.validarLongitud = False
                    obj.addField = False

                else:
                    write(file,path)
                    obj.Validartipo = False
                    obj.validarLongitud = False

                print("Fields added")
            else:
                obj.Validartipo = False
                obj.validarLongitud = False
                tabla(file,path)
        else:
            print("Syntax Error")
            obj.campo.clear()
        return

    except:
        print("error founded")

def validarCampos(atributos,field):
    # try:
        # longitud = len(atributos)
        # campos = []
        # for x in atributos:
        #     #convierte en lista los elementos del .EST
        #     x = str(x).split(",")
        #     # selecciona los elementos del arreglo resultado
        #     for y in x:
        #         characters = "'[] "
        #         for z in range(len(characters)):
        #             y = y.replace(characters[z],"")
        #             campos.append(y)


        print(atributos)
        print(type(atributos))
        print(len(atributos))
        print(atributos[0])
        print(atributos[1])
        print(atributos[2])
        print(type(atributos[0]))
        print(type(atributos[1]))
        print(type(atributos[2]))



            # if type(field) == type(x[1]):
            #     obj.validarFieldType = True
            # else:
            #     print("Not Type Field")
            # if len(field) <= len(x[2]):
            #     obj.validarFieldLen = True
            # else:
            #     print("Not Type Length")
    # except:
    #     print("some")

def write(file,path):
    dat = open(f'/{path}/{file}.est', "w")
    for element in obj.campo:
        dat.write(str(element) + "\n")
    dat.close()
    est = open(f'/{path}/{file}.dat', "w")
    est.close()
    print(obj.campo)
    obj.campo.clear()
    return

def addWrite(file,path):
    path = f'/{path}/{file}.est'
    dat = open( path, "a")

    for element in obj.campo:
        dat.write(str(element) + "\n")

    dat.close()


    print(obj.campo)
    obj.campo.clear()
    obj.addField = False

    return

def deleteWrite(file,path,field):
    path = f'/{path}/{file}.est'
    dat = open( path, "r")
    lines = dat.readlines()
    dat.close()

    del lines[int(field) - 1]

    new_file = open(path, "w+")
    for line in lines:
        new_file.write(line)

    new_file.close()
    dat.close()

    obj.campo.clear()
    obj.addField = False

    return

def InsertWrite(file,path,field):

    path = f'/{path}/{file}.dat'
    dat = open( path, "a")
    for element in field:
        dat.write(str(element) + "\n")
    dat.close()

    return

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
            print('; ERROR')
    except OSError:
        print("DB created fail")

def borrarDB():
    try:
        directory = input('Borra base ')
        com = re.findall(";$",directory)
        if com:
            directory = directory.replace(";","")
            path = os.path.join(parent_dir, directory)
            shutil.rmtree(path)
            print("DB removed successfully")
        else:
            print("; ERROR")
    except OSError:
        print("DB removed fail")

def MuestraDB():
    dir_list = os.listdir(parent_dir)
    for item in dir_list:
        print(f"DB name: {item}")

def usaDB():
    try:
        obj.validarUsebase = True
        DBname = input("Usa base ")
        com = re.findall(";$",DBname)
        if com:
            DBname = DBname.replace(";","")
            path = os.path.join(parent_dir,DBname)
            os.chdir(path)
            currentPath()
            print(f"DB selected {DBname}")
        else:
            print("; ERROR")
            obj.validarUsebase = False
    except OSError:
        print("DB moved fail")
        obj.validarUsebase = False



def insertTable():
    # try:
        if obj.validarUsebase:
            n = 0
            cP = os.getcwd()
            lista = os.listdir(cP)

            file = input("Inserta en ")

            lines = linecache.getlines(file + ".est")
            lines = str(lines)
            lines = lines.replace("\\n","")
            # lines = lines.replace("\'","")
            characters = "\'[] \n \" "

            for z in range(len(characters)):
                lines = str(lines).replace(characters[z],"")

            linee = list(lines.split(","))
            print(linee)


            for files in lista:
                if file + ".dat" in  files:
                    obj.fileExist = True


            if obj.fileExist:
                for x in lista:
                    if file + ".est" in x:
                        tabla = x
                        print(tabla + " --> ")

                        f = open(x,"r")
                        for line in f:
                            n = n + 1
                            print(f'C{n} ' + "\t" + line + "\n")
                        f.close

                        field = input("Campo: ")
                        validarCampos(linee,field)


                # if obj.validarFieldType & obj.validarFieldLen:
                #     InsertWrite(file,cP,field)
                #     obj.fileExist = False

                else:
                    print("Error Founded")
            else:
                print("File Not Exist")
        else:
            print("Select DB first")
    # except:
    #     print("Something Wrong Happened")


def createTable():
    try:
        if obj.validarUsebase:

            cP = os.getcwd()
            lista = os.listdir(cP)

            file = input("Crea tabla ")

            for files in lista:
                files = files.replace(".dat","")
                files = files.replace(".est","")

                if file == files:
                    obj.fileExist = True

            if not obj.fileExist:
                path = os.getcwd()
                tabla(file,path)
            else:
                print("File Exist")
                obj.fileExist = False
        else:
            print("Select a DB first")
    except OSError:
        print("file created fail")

def deleteTable():
    try:
        if obj.validarUsebase:
            files = input("Borra tabla ")
            com = re.findall(";$",files)
            files = files.replace(";","")
            archivo = files.split(",")
            if com:
                ruta = os.getcwd()
                for item in archivo:
                    path1 = os.path.join(ruta, item + ".dat")
                    path2 = os.path.join(ruta, item + ".est")
                    os.remove(path1)
                    os.remove(path2)
                    print(f"File {item} deleted successfully")
            else:
                print("; ERROR")
        else:
            print("Select a DB first")
    except OSError:
        print("File deleted fail")

def showTables():
    try:
        if obj.validarUsebase:
            cP = os.getcwd()
            ls = os.listdir(cP)
            n = 0

            for x in ls:

                if ".est" in x:
                    tabla = x
                    print(tabla + " --> ")

                    f = open(x,"r")

                    for line in f:
                        n = n + 1
                        print(f'C{n} ' + "\t" + line)
                    f.close
                    n = 0

        else:
            print("Select a DB First")
    except:
        print("Something wrong happened")

def addTableField():
    try:
        if obj.validarUsebase:

            cP = os.getcwd()
            lista = os.listdir(cP)


            obj.addField = True
            file = input("Agrega Campo ")


            for files in lista:
                if file + ".est" in  files:
                    obj.fileExist = True

            if obj.fileExist:
                path = os.getcwd()
                tabla(file,path)
                obj.fileExist = False
            else:
                print("File Not Exist")
        else:
            print("Select DB first")
    except:
        print("Something Wrong Happened")

def deleteTableField():
    try:
        if obj.validarUsebase:

            cP = os.getcwd()
            lista = os.listdir(cP)


            file = input("Borra Campo ")

            for files in lista:
                if file + ".est" in  files:
                    obj.fileExist = True

            if obj.fileExist:
                field = input(" ")
                com = re.findall(";$",field)
                field = field.replace(";","")

                if com:
                    deleteWrite(file,cP,field)
                    obj.fileExist = False
                else:
                    print("; ERROR")
            else:
                print("File Not Exist")
        else:
            print("Select DB first")
    except:
        print("Something Wrong Happened")



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
    opcion = ["path base","inserta en","agrega campo","borra campo","usa base","exit","muestra tablas;","muestra bases;","crea base","borra base","crea tabla","borra tabla","clear","help"]

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
        elif opcion == "muestra tablas;":
            showTables()
        elif opcion == "agrega campo":
            addTableField()
        elif opcion == "borra campo":
            deleteTableField()
        elif opcion == "inserta en":
            insertTable()
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