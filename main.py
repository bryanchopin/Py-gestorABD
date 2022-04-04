# import os

# def pedirNumeroEntero():

#     correcto=False
#     num=0
#     while(not correcto):
#         try:
#             num = int(input("Introduce un numero entero: "))
#             correcto=True
#         except ValueError:
#             print('Error, introduce un numero entero')

#     return num



# salir = False
# opcion = 0 #se inicia variable opcion

# while not salir:

#     print ("Elige una opcion")

#     opcion = pedirNumeroEntero()

#     if opcion == 1:
#         print ("Opcion 1")
#     elif opcion == 2:
#         print ("Opcion 2")
#     elif opcion == 3:
#         print("Opcion 3")
#     elif opcion == 4:
#         salir = True
#     else:
#         print ("Introduce un numero entre 1 y 3")

# print ("Fin")




def pedircomando():
    correcto=False
    comando=["uno","dos","tres","cuatro"]
    while(not correcto):
        try:
            num = str(input("Introduce comando: "))
            correcto=True
        except ValueError:
            print('Error, introduce un comando valido')

    return num






def menu():
    salir = False
    opcion = ["uno","dos","tres","cuatro"] #se inicia variable opcion

    while not salir:

        print ("Elige una opcion")

        opcion = pedircomando()

        if opcion == "uno":
            print ("Opcion 1")
        elif opcion == "dos":
            print ("Opcion 2")
        elif opcion == "tres":
            print("Opcion 3")
        elif opcion == "cuatro":
            salir = True
        else:
            print ("Introduce un comando valido")

    print ("Fin")

menu()