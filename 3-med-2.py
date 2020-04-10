str_ip = input()
string = list(str_ip)
vowels = ['A', 'E', 'I', 'O', 'U']
consonants = []

substrings = []
stuart = 0
kevin = 0
for i in range(len(str_ip)):
    if(vowels.count(str_ip[i])):
       kevin = kevin + len(str_ip) - i
    else:
       stuart = stuart + len(str_ip) - i

#substrings = list(dict.fromkeys(substrings))

if(kevin == stuart):
    print("Draw")
else:
    (print("Kevin", kevin)) if (kevin > stuart) else (print("Stuart", stuart))
