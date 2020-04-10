t = int(input())
for iter in range(t):
    flag = 0
    n = int(input())
    mat = []
    for i in range(n):
        temp = list(map(int, input().split(' ')))
        mat.append(temp)

    balls = [0]*n
    containers = [0]*n

    for i in range(n):
        for j in range(n):
            balls[j] += mat[i][j]
            containers[i] += mat[i][j]

    balls = sorted(balls)
    containers = sorted(containers)
    
    for i in range(n):
        if(balls[i] != containers[i]):
            flag = 1
            break

    if(flag == 0):
        print('Possible')
    else:
        print('Impossible')
            
