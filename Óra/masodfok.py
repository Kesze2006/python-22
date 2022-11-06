import math
#a*x2+b*x+c
a = ""
while a == "":
    try:
        a = int(input("a="))
    except:
        print("Érvénytelen érték!")
b = ""
while b== "":
    try:
        b = int(input("b="))
    except:
        print("Érvénytelen érték!")
c = ""
while c == "":
    try:
        c = int(input("c="))
    except:
        print("Érvénytelen érték!")


#(-b+-gyök(b2-4ac) )/ 2a
diszkriminans = b*b-4*a*c
if diszkriminans < 0:
    print("Nincs megoldás")
elif diszkriminans == 0: 
    megoldas = -b / (2*a)
    print("1 megoldás: {}".format(megoldas))
else:
    x1 = (-b+math.sqrt(diszkriminans)) / (2*a)
    x2 = (-b-math.sqrt(diszkriminans)) / (2*a)
    print(x1)
    print(x2)

#gyok = math.sqrt(b*b-4*a*c)
#print(gyok)

