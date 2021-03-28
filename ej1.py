def numeroPrimo(x):
    primo = True
    i=2
    while ((i<=x-1)and primo==True):
        if(x%i==0):
            primo=False
        i+=1
    return primo
  


print("Introduzca un numero")
num = int(input())

resultado=numeroPrimo(num)
print(resultado)
