(n,m) = input().split(' ')

ints = input().split(' ')

a =  dict.fromkeys(input().split(' '))
b = dict.fromkeys(input().split(' '))
p = 0
n = 0

for i in ints:
    if(i in a):
        p = p + 1
    elif (i in b):
        n = n + 1

print(p-n)
