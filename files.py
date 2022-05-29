import os
contenido = open("DB/a.dat", "r")



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

