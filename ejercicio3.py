"""
M = [[1,2,3,4,5],[4,-10,6,4,5],[7,8,9,2,3][7,3,12,4,5],[2,34,12,4,1]]
i = 0
suma = 0
while (i<len(M)):
    j=0
    while(j<len(M[i])):
        if (i != j):
            suma+=M[i][j]
        else:
            print(M[i][j])
        j+=1
    i+=1
"""
M = [[1,2,3,5,7],[4,-10,6,4,5],[7,8,9,2,3],[4,-10,6,4,5],[7,8,9,2,3]]
i = 0
suma = 0
while (i < len(M)):
    j=0
    while (j < len(M[i])):
        if (i != j):
            suma += M[i][j]
        else:
            print(M[i][j])
        j+=1    
    i+=1
print(suma)
