from itertools import combinations
n,m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
answer = 0
flag = 0
for i in range(1,n+1):
    for j in combinations(arr, i):
        flag= 0
        #print(list(j))
        for k in combinations(j, 2):
            if(sum(k) % m == 0):
                flag = 1
                break
            
        
        if(flag == 0):
            answer = len(j)
print(answer)
