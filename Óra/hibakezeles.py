lista = ["Bence","László","Ferenc"]
lista.append("Oszkár")

try:
    print (lista[3])
except:
    print ("Valami nem jó")
else:
    print("Sikeres lefutás")
finally:
    print("Ez a vége")
szam="" 
while szam == "" : 
    try:
         szam = int(input("Kérek egy számot: "))
    except ValueError as e:
        print(e)
        print ("Ez nem szám!")
    except IndexError:
        print("Ismeretlen hiba")

print(szam)
