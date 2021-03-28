'''
i = 0
print(len(M))
while (i < len(M)):
    print("fila",M[i],"longitud col", len(M[i]))
    j=0
    while (j < len(M[i])):
        if (M[i][j] == 6):
            M[i][j] = 999
        print(M[i][j],' ', end= "")
        j+=1
    print()
    i+=1
'''
A = ['ave', 'gatos', 'perro']


i = 0
print(len(A))
while (i < len(A)):
    j=0
    while (j < len(A[i])):
        v = A[i]
        #????
        
        print(A[i][j],"-",end="")
        j+=1
   
    print()
    i+=1
