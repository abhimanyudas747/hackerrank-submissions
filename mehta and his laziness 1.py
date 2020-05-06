import math
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a, a)


def func():
    n = int(input())
    factors = []
    len = 0
    for i in range(1, math.floor(n**0.5)+1):
        if(n % i == 0):
            factors.append(i)
            if(n/i != i and i != 1):
                factors.append(n//i)
                len += 2
            else:
                len += 1
    #print(factors)
    cnt = 0
    for i in factors:
        if(i % 2 == 0 and int(i**0.5) == i**0.5):
            cnt += 1
    if(cnt == 0):
        print(0)
        return
    k = gcd(cnt, len)
    print(str(cnt//k)+"/"+str(len//k))
    return


    
t = int(input())
for i in range(t):
    func()
