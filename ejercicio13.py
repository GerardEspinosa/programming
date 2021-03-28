"""
l = ["la","casa","de","don","salames"]

mayor = 0
for i in range (len(l)):
    if (len(l[i])>mayor):
        may = len(l[i])
print (may)

sup_inf = ""
for i in range (may+4):
    sup_inf = sup_inf + "*"
print(sup_inf)

for i in range(len(l)):
    cadena = ""
    cadena = "* " + l[i]
    for j in range(mayor - len(l[i])):
        cadena = cadena + " "
    cadena = cadena + " *"
    print (cadena)
print(sup_inf)
"""
l =["la","casa","de","don","salames"]
may = 0
for i in range(len(l)):
    if ( len(l[i]) > may ):
        may = len(l[i])

sup_inf = ""
for i in range(may + 4):
    #print("*", end="")
    sup_inf = sup_inf + "*"
    
print(sup_inf)

for i in range(len(l)):
    cadena = ""
    cadena = "* " + l[i]
    for j in range(may - len(l[i])):
        cadena = cadena + " "
    cadena = cadena + " *"
    print(cadena)
    
print(sup_inf)
