M=[]
M=[[1,2,3],[4,5,6],[7,8,9]]
cont=1
i=0
while (i<3):
    a=[]
    j=0
    while (j<3):
        a.append(cont)
        cont+=1
        j+=1
    M.append(a)
    i+=1

print (M)

i=0
while (i<len(M)):
    j=0
    while (j<len(M[i])):
        print (M[i][j],'_',end="")
        j+=1
    print()
    i+=1

aux = []

aux = M[0]
M[0]=M[2]
M[2] = aux

print (M)

may = M[0][0]
men = M[0][0]
i=0
while (i<len(M)):
    j=0
    while (j<len(M[i])):
        if (may < M [i][j]):
            may = M[i][j]
        if (men > M[i][j]):
            men = M[i][j]
        j+=1
    i+=1
print (may,men)
        
