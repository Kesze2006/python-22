import math
szam = [12,14,15,23,45,67,89,78]
#for i in range(8):
    #szam.append(int(input("Kérek egy számot: ")))

for i in szam:
    print(int(i),end=" ")

print()

for i in range(8):
    if i%4==0:
        print()
    print(szam[i],end=" ")


print()

print(sum(szam))


szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

betu = input("Adj meg egy betüt: ")




alma=[]
for e in szoveg:
    if betu==e:
        alma.append(1)
    else:
        pass

print(sum(alma))



print(szoveg[::-1])


print(len(szoveg))

szoveg=szoveg.replace("orna","")

print(len(szoveg))


l=45


l = int(input("Kérek egy számot: "))

fa="""
   *
  ***
 *****
*******
  ***
 *****
*******
  ***
 *****
*******
   *
  ***   """

fa=fa.replace("*",str(l))
print(fa)



szoveg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis ipsum et nisi porta convallis. Sed non bibendum felis. Maecenas porttitor ligula ut hendrerit placerat. Fusce cursus tincidunt lectus. Praesent consequat scelerisque elit, vestibulum placerat justo aliquam ut. Cras lobortis feugiat sagittis. Fusce eleifend interdum lorem ac eleifend. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus luctus velit ac varius gravida. Nulla sit amet vulputate nibh. Cras sed tellus urna. Mauris pulvinar sodales nunc, nec scelerisque risus suscipit quis. Ut ultricies consequat quam, ac condimentum lectus pellentesque quis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin consequat, erat nec gravida ultricies, purus eros pulvinar erat, ut imperdiet enim risus eget purus. Donec magna magna, facilisis non faucibus vel, rhoncus eu elit."















