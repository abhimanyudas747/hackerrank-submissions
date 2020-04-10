def bsearch(arr,start,end, e):
    mid = (start+end)//2
    if(arr[mid] <= e and arr[mid-1] > e):
        return mid
    else:
        if(arr[mid] > e):
            return bsearch(arr, mid, end, e)
        else:
            return bsearch(arr, start, mid, e)
n = int(input())
arr = list(map(int, input().split(' ')))
arr = list(set(arr))
n = len(arr)
arr.sort(reverse=True)
m = int(input())
alice_scores = list(map(int, input().split(' ')))
alice_scores.sort(reverse=True)
rank = []



    




for i in alice_scores:
    if(arr[0] <= i):
        rank.append(1)
    elif(arr[-1] == i):
        rank.append(n)
    elif(arr[-1] > i):
        rank.append(n+1)
        
    else:
        j = bsearch(arr,1, n, i)
        rank.append(j+1)
        
        
for i in rank[::-1]:
    print(i)
