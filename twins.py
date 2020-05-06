import random
def gcd(a,b):
    if(a==0):
        return b
    else:
        return gcd(b%a, a)
def isprime(p):

    a = random.randint(1, 10)
    b = random.randint(10**2, 200)
    c = random.randint(200, 300)
    if(gcd(p,c) != 1):
        print(p,c)
        return False
    d = random.randint(50, 99)
    e = random.randint(10, 120)
    if (((a**p - a) % p == 0) and ((b**p - b) % p == 0) and ((c**p - c) % p == 0) and ((d**p - d) % p == 0) and ((e**p - e) % p == 0)):
        return True
    return False


cnt = 0
n,m = list(map(int, input().split(' ')))
for i in range(n,m-1):
    if(isprime(i) and isprime(i+2)):
        cnt += 1

print(cnt)
