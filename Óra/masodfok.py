import math
#(-b+-gyök(b2-4*a*c))/2*a

#a*x2+b*x+c

def egyenlet(a,b,c):
    szoveg = "0 ="
    if a != 0:
        szoveg += str(a)+"x²"
        
    if b > 0:
        szoveg +="+"+str(b)+"x"
    elif b < 0:
        szoveg +=" "+str(b)+"x"
     
    if c > 0:
        szoveg +="+"+str(c)
    elif c < 0:
        szoveg +=" "+str(c)

    return szoveg


        


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
x1 = ""
x2 = ""
diszkriminans = b*b-4*a*c
if diszkriminans < 0:
    print("Nincs megoldás")
elif diszkriminans == 0: 
    megoldas = -b / (2*a)
    x1 = megoldas
    x2 = megoldas
    print("1 megoldás: {}".format(megoldas))
else:
    x1 = (-b+math.sqrt(diszkriminans)) / (2*a)
    x2 = (-b-math.sqrt(diszkriminans)) / (2*a)
    print("2 megoldás: x1:{}, x2:{}".format (x1,x2))

#gyok = math.sqrt(b*b-4*a*c)
#print(gyok)

print(egyenlet(a,b,c))

print(a)
print(x1)
print(x2)







