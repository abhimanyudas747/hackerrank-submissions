n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

candies=[1]*n

for i in range(n-2+1):
    while(arr[i] > arr[i+1] and not(candies[i] > candies[i+1])):
        #print("arr[i] :", arr[i], "arr[i+1]", arr[i+1])
        candies[i] = candies[i+1] + 1
    while(arr[i] < arr[i+1] and not(candies[i] < candies[i+1])):
        candies[i+1] = candies[i] + 1


for i in reversed(range(n-2+1)):
    while(arr[i] > arr[i+1] and not(candies[i] > candies[i+1])):
        #print("arr[i] :", arr[i], "arr[i+1]", arr[i+1])
        candies[i] = candies[i+1] + 1
    while(arr[i] < arr[i+1] and not(candies[i] < candies[i+1])):
        candies[i+1] = candies[i] + 1




print(sum(candies))
