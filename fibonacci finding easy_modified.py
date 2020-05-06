c = 10**9 + 7
def get_powers(n):
    powers = []
    while(n > 0):
        i = 1
        while((2**i) <= n):
            i += 1
        powers.append(i-1)
        n = n - 2**(i-1)
    return powers

powers = []
def find_power(n):
    mat = [[1,1],[1,0]]
    powers.append(mat)
    mat = [[2,1],[1,1]]
    powers.append(mat)
    for i in range(1,n):
        auxmat = powers[-1]
        mat = powers[-1]
        newmat = [[((mat[0][0]%c * auxmat[0][0]%c)%c + (mat[0][1]%c * auxmat[1][0]%c)%c)%c, ((mat[0][0]%c * auxmat[0][1]%c)%c + (mat[0][1]%c * auxmat[1][1]%c)%c)%c],
                [((mat[1][0]%c * auxmat[0][0]%c)%c + (mat[1][1]%c * auxmat[1][0]%c)%c)%c, ((mat[1][0]%c * auxmat[0][1]%c)%c + (mat[1][1]%c * auxmat[1][1]%c)%c)%c]]
        powers.append(newmat)


inp = []
n = int(input())
max_n = -1
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    inp.append(tmp)
    if(max_n < tmp[-1]):
        max_n = tmp[-1]
find_power(max_n)

    

for i in inp:
    if(i[2] == 1):
        print(i[1])
        continue
    if(i[2] == 0):
        print(i[0])
        continue
    curr_pow = get_powers(i[2]-1)
    auxmat = powers[curr_pow[0]]
    for j in range(1,len(curr_pow)):
        mat = powers[curr_pow[j]]
        auxmat = [[mat[0][0] * auxmat[0][0] + mat[0][1] * auxmat[1][0], mat[1][0] * auxmat[0][0] + mat[1][1] * auxmat[1][0]],
                [mat[0][0] * auxmat[0][1] + mat[0][1] * auxmat[1][1], mat[1][0] * auxmat[0][1] + mat[1][1] * auxmat[1][1]]]
    ans = auxmat[0][0] * i[1] + auxmat[0][1] * i[0]
    print(ans%c)
        
        
        
    
