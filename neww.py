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




