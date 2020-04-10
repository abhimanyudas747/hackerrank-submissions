import random
(k, m) = input().split(" ")
k = int(k)
m = int(m)
biglist = []
sqrs = []
for i in range(k):
    inplst = input().split(" ")
    for j in range(len(inplst)):
        inplst[j] = abs(int(inplst[j]))
    biglist.append(inplst[1:])


op = 0
iters = 10000
for i in range(iters):
    for j in biglist:
        sqrs.append(random.choice(j)**2)
    temp = sum(sqrs)%m
    sqrs = []
    if(op < temp):
        op = temp



print(op)
