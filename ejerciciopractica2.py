m = [
    ["casa","gestion","ciudadano"],
    ["base","datos","digito"],
    ["cadena","presentacion","control"],
    ]
inicio = "ca"
retorno = []
salir = False
cadena = ""
z = 0
j=0
i = 0
while (i<len(m)):
    j=0
    while (j < len(m[i])):
        cadena = m[i][j]
        index = 0
        z = 0
        salir = False
        while (z<len(cadena)and not salir):
            if (cadena[z]==inicio[index]):
                index+=1
                if (index == len(inicio)):
                    salir = True
            else:
                salir = True
            z+=1
        if(index == len(inicio)):
            retorno.append(cadena)
        j+=1
    i+=1
print(retorno)
    
