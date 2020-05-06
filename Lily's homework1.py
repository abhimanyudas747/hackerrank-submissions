n = int(input())
arr = list(map(int, input().split(' ')))
index_map = [*(enumerate(arr))]
index_map_rev = sorted(index_map, key=lambda x: x[1], reverse=True)
index_map.sort(key=lambda x: x[1])

err = 0
err_rev = 0
for i in range(n):
    if(arr[i] != index_map[i][1]):
        err += 1

for i in range(n):
    if(arr[i] != index_map_rev[i][1]):
        err_rev += 1

if(err_rev < err):
    index_map = index_map_rev.copy()
node_map = [[i[0],i[1][0]] for i in enumerate(index_map)]
cycle_sizes = []
visited = dict.fromkeys(range(n), "N")

for i in range(n):
    if(visited[i] == "N"):
        visited[i] = 'Y'
        pointer = i
        size = 0
        while(visited[node_map[pointer][1]] != 'Y'):
            size += 1
            visited[node_map[pointer][1]] = 'Y'
            pointer = node_map[pointer][1]
        size += 1
        cycle_sizes.append(size)
        size = 0
            
ans = 0
for i in cycle_sizes:
    ans += i-1
print(ans)
