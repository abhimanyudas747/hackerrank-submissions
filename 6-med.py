n = int(input())
words = {}
for i in range(n):
    temp = input()
    try:
        words[temp] = words[temp] + 1
    except Exception as e:
        words[temp] = 1
        
        

#d = dict.fromkeys(words)
print(len(words))
for i in words:
    #d[i] = words.count(i)
    print(words[i], end = " ")
