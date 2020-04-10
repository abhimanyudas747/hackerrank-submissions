
def work():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    ctr = 0
    max_val = 0
    for i in range(n):
        if(arr[i] > max_val):
            ctr += 1
            max_val = arr[i]
            


    
    if(ctr % 2 != 0):
        print("BOB")
    else:
        print("ANDY")

t = int(input())
for iter in range(t):
    work()
