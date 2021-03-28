sec = "12??2455.$%·12"
ascii = 0
aux = ""
lista = []
i = 0
while (i<len(sec)):
    ascii=ord(sec[i])
    if (ascii >= 48 and ascii<=57): #0=48 9=57
        aux = aux+sec[i]
        print (aux)
    else:
        if (len(aux)>0):
            lista.append(aux)
        aux=""
    i+=1
if (len(aux)>0):
    lista.append(aux)

print ("resultado final", lista)
