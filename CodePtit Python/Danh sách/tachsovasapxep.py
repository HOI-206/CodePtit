def tachso(a):
    c = []
    res = ''
    b = ['0','1','2','3','4','5','6','7','8','9']
    for i in a :
        for j in range(0,len(i)):
            if i[j] in b:
                res += i[j]
            else:
                if len(res) != 0 :
                    c.append(int(res))
                res = ''
    if len(res) != 0:
        c.append(int(res))
    
    c.sort()
    print(*c,sep='\n')

n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
tachso(a)