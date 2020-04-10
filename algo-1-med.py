import math
#s_list = []
def encryption(s):
    global s_list
    s = s.replace(' ', '')
    k = len(s)
    u = math.ceil(math.sqrt(k))
    l = math.floor(math.sqrt(k))
    if(u*l < k):
        l = l+1
    if (k < u*l):
        i = k
        while(i < (u*l)):
            s = s + " "
            i = i + 1
    s_list = []
    temp = []
    k = 0
    for i in range(l):
	    for j in range(u):
		    temp.append(s[k])
		    k = k + 1
	    s_list.append(temp)
	    temp = []
    s_list = list(map(list, zip(*s_list)))
    #print(s_list)
    op = ''
    for i in s_list:
            for j in i:
                if(j != " "):
                    op = op + j
            op = op + ' '
    print(op)

encryption("chiilout")

