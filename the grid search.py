def work():
    n,m = list(map(int, input().split(' ')))
    arr = []
    for i in range(n):
        temp = list(map(int, list(input())))
        arr.append(temp)
    n_, m_ = list(map(int, input().split(' ')))
    aux = []
    flag = 0
    for i in range(n_):
        temp = list(map(int, list(input())))
        aux.append(temp)
    for i in range(n-n_+1):
        for j in range(m-m_+1):
            flag = 0
            for k in range(n_):
                for l in range(m_):
                    if(arr[k+i][l+j] != aux[k][l]):
                        flag = 1
            if(flag == 0):
                print("YES")
                return
            
                        
                    

    print("NO")
    return

    




t = int(input())
for iter in range(t):
    work()
    
