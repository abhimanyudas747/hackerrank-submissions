def work():
    n,m = list(map(int, input().split(' ')))
    arr = []
    pat = []
    for i in range(n):
        temp = list(input())
        arr.append(temp)

    global flag
    n_,m_ = list(map(int, input().split(' ')))
    for i in range(n_):
        temp = list(input())
        pat.append(temp)

    
        
    for i in range(n-n_+1):
        for j in range(m-m_+1):
            if(arr[i][j] == pat[0][0] and arr[i+1][j+1] == pat[1][1] and arr[i][j+1] == pat[0][1]):
                flag = 1
                
                
                for k in range(n_):
                    for l in range(m_):
                        if (arr[i+k][j+l] != pat[k][l]):
                            flag = 0

                if(flag == 1):
                    return
        
                
        
t = int(input())
for iter in range(t):
    flag = 0
    work()
    if(flag == 1):
        print("YES")
    else:
        print("NO")

