def work():
    n,k = list(map(int, input().split(' ')))
    indexes = reversed(range(1,n+1))
    included = {}
    answer = []
    for i in indexes:
        if(i+k <= n and included.get(i+k, -1) == -1):
            included[i+k] = 1
            answer.append(i+k)
        elif(i-k >= 1 and included.get(i-k, -1) == -1):
            included[i-k] = 1
            answer.append(i-k)
        else:
            print(-1, end=' ')
            return
    for i in answer[::-1]:
        print(i, end=' ')

t = int(input())
for iter in range(t):
    work()
    print()
