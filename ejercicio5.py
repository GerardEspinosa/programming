#5 lista con longitud fija sin poder hacer un append
i = 0
suma = 0
l1=[]
l2 = [0]*(len(M)*len(M[0]))

# [0] = [0][0]
#[1] =[0][1]
# ...
while (i < len(M)):
    j=0
    while (j < len(M[i])):        
        #l1.append(M[i][j])
        l2[i*(len(M[i])) + j] = M[i][j]
        j+=1    
    i+=1
print(l2)
