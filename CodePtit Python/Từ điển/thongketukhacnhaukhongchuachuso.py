def solve(a):
    w = []
    for i in a:
        i =  i.lower() + ' '
        res = '' 
        for j in i :
            if 'a' <= j <= 'z':
                res += j
            else :
                if res != '':
                    w.append(res)
                    res = ''
    d = {}
    for i in w:
        if i in d:
            d[i] += 1
        else:
            d[i] =1
    x = sorted(d.items(), key = lambda i : (-i[1],i[0]))
    for i , j in x :
        print(i , j)
        

n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
solve(a)