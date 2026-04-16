def solution(a,k):
    w = []
    for i in a :
        i = i.lower() + ' '
        res = ''
        for j in i :
            if ('a' <= j <= 'z') or ('0' <= j <= '9') :
                res += j
            else:
                if res != '':
                    w.append(res)
                    res = ''

    d = {}
    for i in w :
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    x = dict(sorted(d.items(), key = lambda x :(-x[1],x[0])))
    for key in x:
        if x[key] >= k:
            print(key ,x[key])

n,k = map(int,input().split())
a = []
for i in range(n):
    x = input()
    a.append(x)
solution(a,k)