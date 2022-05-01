import json,re

x = []

def hello():
    datos = input("ingresa los datos: ")
    campos = str(datos).split(",")
    com = re.findall(";$",datos)
    if com:
        for cam in campos:
            y = {f"{cam}":""}
            y = str(f'"{y}"')
            x.append(y)
            j = json.dumps(x,indent=4)
            print(j)
    else:
        for cam in campos:
            y = {f"{cam}":""}
            x.append(y)
            hello()






def testt():
      # try:
    datos = input("ingresa los datos: ")
    com = re.findall(";$",datos)

    campos = datos.split(",")
    campos = tuple(campos)

    a = []
    if com:
        for cam in campos:
            cam = ' '
            a.append(cam)

        a = tuple(a)
        w = dict(zip(campos,a))
        j = json.dumps(w,indent=4)
        print(j)
    else:
        testt()
  # except:
  #   print(NameError)
  
  
testt()