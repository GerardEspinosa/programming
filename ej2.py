def numeroPrimo(x):
    primo = True
    i=2
    while ((i<=x-1)and primo==True):
        if(x%i==0):
            primo=False
        i+=1
    return primo
  
i = 1
cont = 0
l=[]
while (cont<100):
    if (numeroPrimo(i)):
        cont+=1
        l.append(i)
    i+=1

print(l)
