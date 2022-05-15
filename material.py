# campo = ['Math.acos,Math.acosh,Math.asin,Math.asinh,Math.atan,Math.atan2,Math.atanh,Math.cos,Math.cosh,Math.sin,Math.sinh,Math.tan,Math.tanh']
# campo = str(campo).replace(",","|")
# print(campo)

# class own:
#     def __init__(self):
#         self.tipos = ["caracteres","entero","decimal","fecha"]

# obj = own()

# atributos =  input("").split(",")
# l = list(filter(lambda x: atributos[1] in x, obj.tipos))
# if l:
#     print(l)
link = False
atributo = input("").split(",")

tipos = ["caracter","entero","decimal","fecha"]

for x in tipos:
    if atributo[1] == x:
        link = True

if len(atributo) == 3 and link:
    print("success")
else:
    print("error")




# l = list(filter(lambda x: atributo[1] in x,py_lst))
# print(l)