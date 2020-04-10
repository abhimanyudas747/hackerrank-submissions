numbers = input()
output = []
flag = 0
i = 0
j = 1
k = i
while(True):
    if(j >= len(numbers)):
        flag = 1
        break
    seg_1 = int(numbers[k:i+1])
    seg_2 = int(numbers[i+1:j+1])
    if(seg_1 == seg_2 - 1):
        output.append(int(seg_1))
        #numbers = numbers[i+1:]
        k = i
        i = j
        j = i + 1
    else:
        j += 1

if(flag == 1):
    print('yes')
        
    
