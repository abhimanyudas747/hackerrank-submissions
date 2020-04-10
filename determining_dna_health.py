import re
n = int(input())
genes = list(input().split(' '))
health_values = list(map(int, input().split(' ')))
m = int(input())
min = 999999
max = -999999


def cal_health(start, end, d):
    iter = 0
    total_health = 0
    for gene in genes[int(start):int(end)+1]:
        gene = r'(?=('+gene+'))'
        k = re.findall(gene, d)
        health_multiplier = len(k)
        total_health += health_values[int(start)+iter] * health_multiplier
        iter += 1

    return total_health
    

for i in range(m):
    start, end, d = input().split(' ')
    health = cal_health(start, end, d)
    if(min > health):
        min = health
    if(max < health):
        max = health

print(min, max)
