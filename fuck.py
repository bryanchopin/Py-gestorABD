import re



l = ['d.est', 'ca.est', 'ca.dat', 'd.dat',"c.est","a.est"]

a = 'a'
Validartipo = False

# for x in l:
#     for y in x:
#         if a == y:
#             Validartipo = True


for x in l:
    x = x.replace(".est","")
    x = x.replace(".dat","")
    print(x)
    if a == x:
        Validartipo = True




if Validartipo:
    print("hola")
else:
    print("mamaste")