import re
(n, m) = map(int, input().split(' '))
mat = []
for i in range(n):
    temp_list = list(input())
    mat.append(temp_list)
    temp_list = ''

string_list = []
string = ''
for i in range(m):
    for j in range(n):
        string_list.append(mat[j][i])
for i in range(m*n):
    string = string+string_list[i]

string = re.sub(r"(?<=\w)\W+(?=\w)"," ", string)
print(string)
