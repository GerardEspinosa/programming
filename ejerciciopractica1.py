m = [
    ["casa","gestion","ciudadano"],
    ["base","datos","digito"],
    ["cadena","presentacion","control"],
    ]
letra = "d"
retorno = []
existe = False
cadena = ""
z = 0
j=0
i = 0
while (i<len(m)):
    j=0
    while (j < len(m[i])):
        cadena = m[i][j]
        existe = False
        z = 0
        while (z<len(cadena) and not existe):
            if (cadena[z]) == letra:
                existe = True
            z+=1
        if (existe):
            retorno.append(cadena)
        print (m[i][j])
        j+=1
    i+=1
print(retorno)
    
    
