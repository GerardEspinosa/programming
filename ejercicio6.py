import random

M = [[1,2,3,5,7],[4,-10,6,4,5],[7,8,9,2,3],[4,-10,6,4,5],[7,8,9,2,3]]

i = 0
while (i < len(M)):
    j=0
    while (j < len(M[i])):
        M[i][j] = random.randint(-9,9)           
        j+=1    
    i+=1
#print(M)
for i in range(len(M)):
    print(M[i])

pos = 0
neg = 0
cero = 0

i = 0
while (i < len(M)):
    j=0
    
    while (j < len(M[i])):
        if (M[i][j]> 0):
            pos+=1
        elif(M[i][j]< 0):
            neg+=1
        else:
            cero+=1            
        j+=1    
    i+=1

print("pos",pos,"neg",neg,"ceros",cero)
