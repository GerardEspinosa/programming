#funcion - retorna algo
def suma(x,y): # lista parametros
    total = x + y     
    return total

#procedimiento no retorna
def mensaje(idioma):
    print("############")
    if (idioma == 1):
        print("Missatge en català")
    elif (idioma == 2):
        print("Mensaje en castellano")
    else:
        print("No existe opcion")
    print("############")

#programa

a = 3
b = 4

mensaje(4)

c = suma(a,b)
c = 4 + suma(a,b) + suma(a,b)

c = suma(a,a)

print(suma(3,b))

print(c)
