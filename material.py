import re

campo = []

def tabla():
      Atributos = input("")
      com = re.findall(";$",str(Atributos))
      Atributos = Atributos.replace(";","")
      Latrib = Atributos.split(",")
      if len(Latrib) > 3:
            print("field error")
      else:
        campo.append(Latrib)
        if com:
          print (campo)
        else:
            tabla()

tabla()