import numpy as np
n,m = list(map(int, input().split(' ')))
x = input().split(' ')
y = input().split(' ')
aux = ['']*(n+2)
mat = []
for i in range(m+2):
    mat.append(aux.copy())
    

for i in range(2,m+2):
    for j in range(2,n+2):
        if(y[i-2] == x[j-2]):
            mat[i][j] = mat[i-1][j-1]+' '+x[j-2]
        else:
            if(len(mat[i-1][j]) > len(mat[i][j-1])):
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i][j-1]

#print(' '.join(list(mat[-1][-1])))
print(mat[-1][-1])
