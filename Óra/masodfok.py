import math
#a*x2+b*x+c

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))


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

