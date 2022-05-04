import re







campos = []

def result(campos):
    print(campos)
    return


def tablaa():
    Atributos = input("")
    com = re.findall(";$",str(Atributos))
    Atributos = Atributos.replace(";","")
    Latrib = Atributos.split(",")
    while com:
        
        if len(Latrib) > 3:
            print("field error")
        else:
            campos.append(Latrib)
            if com:
                result(campos)
            else:
                tabla()


def tabla():
    Atributos = input("")
    com = re.findall(";$",str(Atributos))
    Atributos = Atributos.replace(";","")
    Latrib = Atributos.split(",")
    if len(Latrib) > 3:
        print("field error")
    else:
        campos.append(Latrib)
        if com:
            result(campos)
        else:
            tabla()

# def main():
tabla()

# main()



# find new issue, incorrect evaluation in if
def createTable():
    try:
        if obj.active > 1:
            files = input("Crea tabla ")
            com = re.findall(";$",files)
            files = files.replace(";","")
            archivo = files.split(",")
            if com:
                archivo = list(files)
                path = os.getcwd()

                obj.tabla()

                for item in archivo:
                    dat = open(f'/{path}/{item}.dat', "w")
                    for element in obj.result():
                        dat.write(element + "\n")
                    dat.close()
                    est = open(f'/{path}/{item}.est', "w")
                        # file.write("Primera línea" + os.linesep)
                        # file.write("Segunda línea")
                    est.close()
                    print(f'file {item} created successfully')
            else:
                print("; ERROR")
        else:
            print("Select a DB first")
    except OSError:
        print("file created fail")


