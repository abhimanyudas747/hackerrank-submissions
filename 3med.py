str_ip = input()
string = list(str_ip)
vowels = []
consonants = []
for i in string:
    if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels.append(i)
    else:
        consonants.append(i)

vowels = list(dict.fromkeys(vowels))
consonants = list(dict.fromkeys(consonants))

substrings = []

for i in range(len(str_ip)+1):
    for j in  range(i+1, len(str_ip)+1):
        substrings.append(str_ip[i:j])

#substrings = list(dict.fromkeys(substrings))

stuart = 0
kevin = 0
k=-1
for i in vowels:
    for j in substrings:
        if(i == j[0]):
            kevin = kevin + 1
for i in consonants:
    for j in substrings:
        if(i == j[0]):
            stuart = stuart + 1
if(kevin == stuart):
    print("Draw")
else:
    (print("Kevin", kevin)) if (kevin > stuart) else (print("Stuart", stuart))
