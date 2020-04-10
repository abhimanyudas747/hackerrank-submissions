n,m = list(map(int, input().split(' ')))
queries = []
temp = []
arr = [0]*n
max = 0
curr = []
for i in range(m):
    temp = list(map(int, input().split(' ')))
    arr[temp[0]-1] += temp[2]
    if(temp[1] < n):
        arr[temp[1]] -= temp[2]
        
x = 0
for i in arr:
    x += i
    if(max < x):
        max = x
print(max)
        
        
