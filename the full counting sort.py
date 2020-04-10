class element:
    def __init__(self, rank, string):
        self.rank = rank
        self.string = string

def getrank(e):
    return e.rank
n = int(input())
arr = []
k = 0
for i in range(n):
    temp = list(input().split(' '))
    if(k<n//2):
        arr.append(element(int(temp[0]), '-'))
    else:
        arr.append(element(int(temp[0]),temp[1]))
    k += 1
arr = sorted(arr, key=getrank)
for i in arr:
    print(i.string, end=' ')
