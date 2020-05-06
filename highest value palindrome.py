n,m = list(map(int, input().split(' ')))
k = m
arr = list(input())
numchanges = 0
flag = 1
changedict = {}
for i in range(n//2):
    if(arr[i] < arr[n-1-i]):
        if(m <= 0):
            print(-1)
            flag = 0
            break
        arr[i] = arr[n-1-i]
        m -= 1
        changedict[i] = 1
        changedict[n-1-i] = 1
        numchanges += 1
    elif(arr[n-1-i] < arr[i]):
        if(m <= 0):
            print(-1)
            flag = 0
            break
        arr[n-1-i] = arr[i]
        m -= 1
        changedict[i] = 1
        changedict[n-1-i] = 1
        numchanges += 1

#print(arr)



for i in range(n//2+1):
    if(arr[i] != '9' and arr[n-1-i] != '9' and m > 0):
        
        if(changedict.get(i,-1) == -1 and m >1):
            arr[i] = arr[n-1-i] = '9'
            m -= 2
        elif(changedict.get(i,-1) == 1):
            arr[i] = arr[n-1-i] = '9'
            m -= 1
        elif(i == n//2 and n%2 != 0):
            arr[i] = arr[n-1-i] = '9'
            m-= 1
        else:
            continue



if(flag == 1):
    print(''.join(arr))
