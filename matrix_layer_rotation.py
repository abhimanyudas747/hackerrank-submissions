def rotatematrix(a):
    
    top = 0
    bottom = len(a)-1
    left = 0
    right = len(a[0])-1
    st = 0


    while(top < bottom and left < right):

        prev = a[st][st+1]
        for i in range(top,bottom+1):
            curr = a[i][left]
            a[i][left] = prev
            prev = curr
            
        left += 1

        for i in range(left, right+1):
            curr = a[bottom][i]
            a[bottom][i] = prev
            prev = curr

        bottom -= 1

        for i in reversed(range(top, bottom+1)):
            curr = a[i][right]
            a[i][right] = prev
            prev = curr

        right -= 1

        for i in reversed(range(left, right+1)):
            curr = a[top][i]
            a[top][i] = prev
            prev = curr

        top += 1
        st = st + 1

    return a



n,m,r = list(map(int, input().split(' ')))
mat = []
for i in range(m):
    temp = list(map(int, input().split(' ')))
    mat.append(temp)

for i in range(r):
    mat = rotatematrix(mat)


for i in range(n):
    for j in range(m):
        print(mat[i][j], end=' ')

    print('')
