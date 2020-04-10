n, p = list(map(int, input().split(' ')))
temp = []
pairs = []
for i in range(p):
    temp = list(map(int, input().split(' ')))
    paris.append(temp)


aux_arr = pairs[0]
pair_dict = dict.fromkeys(aux_arr, 0)
for i in range(1, p):
    for j in range(2):
        if(pairs[i][j] in aux_arr):
            
            
