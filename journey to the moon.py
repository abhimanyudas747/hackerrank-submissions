n,m = list(map(int, input().split(' ')))
arr = [-1]*n
def find(e, i):
    try:
        if(arr[e] < 0):
            return (e, i)
        else:
            return find(arr[e], i+1)
    except:
        print(e, i)
        return


def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n * factorial(n-1)



pairs = 1
pair_cnt = 0
singles = 0
answer =0
for i in range(m):
    temp = list(map(int, input().split(' ')))
    m1,m2 = find(temp[0], 1)
    m3,m4 = find(temp[1], 1)
    if(m1 == m3):
        continue
    if(arr[m1] <= arr[m3]):
        arr[m1] -= m4
        arr[m3] = m1
    else:
        arr[m3] -= m2
        arr[m1] = m3
    print(arr)
    if(arr[2] == 2):
        print(temp)
        break


for i in arr:
    if (i < -1):
        pairs *= -i
        pair_cnt += 1
    elif(i == -1):
        singles += 1

if(pair_cnt <= 1):
    for i in range(singles):
        answer += n-singles
        
else:
    answer = pairs
    for i in range(singles):
        answer += n-singles

answer += factorial(singles)/(factorial(singles-2) * 2)
print(int(answer))
    
    
