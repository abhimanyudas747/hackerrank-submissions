n,k = list(map(int, input().split(' ')))
costs = list(map(int, input().split(' ')))
bought = [0]*k
costs.sort(reverse=True)
cnt = 0
min_cost = 0
while(cnt < n):
    try:
        for i in range(k):
            
            min_cost += (bought[i] + 1) * costs[cnt+i]
            bought[i] += 1
    except:
        break
    cnt = cnt+i+1
    
print(min_cost)
