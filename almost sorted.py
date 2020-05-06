import random
def almostSorted(arr):
    arr_sorted = sorted(arr)
    #check if swap possible
    errors = []
    for i in range(len(arr)):
        if(arr[i] != arr_sorted[i]):
            errors.append(i+1)
    if(len(errors) == 2):
        print("yes")
        print("swap", errors[0], errors[1])
        return
    #check if contagious
    for i in range(len(errors)-1):
        if(errors[i]+1 != errors[i+1]):
            contagious = 0
            break
        contagious = 1
    if(contagious == 1):
        arr[errors[0]-1:errors[-1]] = reversed(arr[errors[0]-1:errors[-1]])
    #check by reversing
    
    for i in range(len(arr)):
        if(arr[i] != arr_sorted[i]):
            possible = 0
            break
        possible = 1
    if(possible == 0):
        print("no")
    else:
        print("yes")
        print("reverse", errors[0], errors[-1])


n = int(input())
arr = list(map(int, input().split(' ')))
almostSorted(arr)
