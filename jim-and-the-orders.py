n = int(input())
orders = []
output = []

def func(i):
    return sum(orders[i-1])

for i in range(n):
    temp = list(map(int, input().split(' ')))
    orders.append(temp)
    output.append(i+1)

output = sorted(output, key=func)
    
for i in output:
    print(i, end=' ')
