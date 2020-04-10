t = int(input())
answers = []
for k in range(t):
    n = int(input())
    cubes = list(map(int, input().split(" ")))
    stack = [999999999999]
    flag = 0
    j = n-1
    i = 0
    while(i <= j ):
        if(stack[-1] >= cubes[i] or stack[-1] >= cubes[j]):
            if(cubes[i] >= cubes[j] and stack[-1] >= cubes[i]):
                stack.append(cubes[i])
                #print("push",cubes[i]);
                i = i + 1
                
            elif(cubes[j] > cubes[i] and stack[-1] >= cubes[j]):
                stack.append(cubes[j])
                #print("push",cubes[j])
                j = j - 1
            else:
                flag = 1
                break
               
        else:
            flag = 1
            break
    #print(stack)
    if(flag == 1):
        answers.append("No")
    else:
        answers.append("Yes")
for i in answers:
    print(i)

