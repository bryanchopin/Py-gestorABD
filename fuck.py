l = ['x','1.3','12']
print(str.isdigit(l[0]))
print(float(l[1]))
print(str.isdigit(l[2]))

if '.' in l[1]:
    print(l[1])
    print("awebo es float")
    print(type(l[1]))
    l[1]= float(l[1])
    print(l[1])
    print(type(l[1]))
else:
    print("mamaste")
