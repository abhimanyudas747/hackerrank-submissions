t = int(input())
for iter in range(t):
    len = int(input())
    arr = list(map(int, input().split(' ')))
    subseq_sum = 0
    flag = 0
    for i in arr:
        if(i > 0):
            subseq_sum += i
            flag = 1

    aux_mat = []
    
    
    for i in range(len+1):
        temp = [0]*(len+1)
        aux_mat.append(temp)
            
    subarr_sum = 0
    for i in range(len):
        for j in range(i+1,len+1):
            aux_mat[i][j] = aux_mat[i][j-1] + arr[j-1]
            if(subarr_sum < aux_mat[i][j]):
                subarr_sum = aux_mat[i][j]
        
    if(flag == 0):
        subarr_sum = max(arr)
        subseq_sum = max(arr)
    

    print(subarr_sum, subseq_sum)
            
