def ktra(a,m):
    res = []
    maxv = max(a)
    idx = a.index(maxv)
    a.insert(idx,m)
    am = []
    duong = []
    for i in a:
        if i < 0 :
            am.append(i)
        else:
            duong.append(i)
    for i in am : 
        res.append(i)
    for i in duong : 
        res.append(i)
    return res


t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    a = ktra(a,m)
    print(*a)