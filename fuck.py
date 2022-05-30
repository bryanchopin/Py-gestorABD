import re



# l = ['d.est', 'ca.est', 'ca.dat', 'd.dat',"c.est","a.est"]

# a = 'a'
# Validartipo = False

# for x in l:
#     for y in x:
#         if a == y:
#             Validartipo = True


# for x in l:
#     x = x.replace(".est","")
#     x = x.replace(".dat","")
#     print(x)
#     if a == x:
#         Validartipo = True




# if Validartipo:
#     print("hola")
# else:
#     print("mamaste")

c1 = "['12', 'entero', '23'],['12', 'entero', '23']"
# c1 = str(c1).replace('""',"")
c1 = str(c1).replace("'","")
c1 = str(c1).replace("[","")
c1 = str(c1).replace("]","")
c2 = c1.split(",")


c1 = list()
print(c2)
print(type(c2))
print(str.isnumeric(c2[0]))
print(c2[1])
print(c2[2])
for x in c2:
    print (x)
print(type(c4))