def func(x,n,t):
    #print(x,n,t)
    max_num = 0
    if(x==0):
        return 1
    if(x<0):
        return 0
    for i in range(t,100):
        max_num += func(x-(i**n), n, i+1)
    return max_num

x = int(input())
n = int(input())
print(func(x,n,1))
