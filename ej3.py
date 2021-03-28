def intercambio(x,y):
    aux = x[0]
    x[0] = y[0]
    y[0] = aux
    
a = [23]
b = [56]
print(a,b)
intercambio(a,b)
print(a,b)
