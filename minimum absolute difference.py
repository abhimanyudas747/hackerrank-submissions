n = int(input())
arr = list(map(int, input().split(' ')))
arr = list(sorted(arr, reverse=True))
print(arr[0]-arr[1])
