isbn = [[8,4,2,0,5,3,2,1,1,8],
        [8,4,7,5,2,2,3,3,2,'X'],     
        [8,4,7,5,2,2,3,3,1,'X']        
        ]

total = 0
digc = 0
for i in range(len(isbn)):
    isb = isbn[i]
    total = 0
    digc = 0
    if (len(isb) == 9):
        for j in range (len(isb) - 1):
            total = total + isb[j]*(j+1)
        digc = total % 11

        if (isb[9] == 'X' and digc == 10):
            print(isb, "isbn correcto")
        elif (digc == isb[9]):
            print(isb,"isbn correcto")
        else:
            print(isb, "isbn incorrecto")
            """
    else: # caso 13 digitos
        for j in range (len(isb) - 1):
            total = total + isb[j]*(j+1)
        digc = total % 11

        if (isb[12] == 'X' and digc == 10):
            print(isb, "isbn correcto")
        elif (digc == isb[12]):
            print(isb,"isbn correcto")
        else:
            print(isb, "isbn incorrecto")
"""
