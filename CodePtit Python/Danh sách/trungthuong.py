def trung(a):
    dem = {}
    for i in a :
        if i in dem:
            dem[i]+=1
        else:
            dem[i]=1
    solan = max(dem.values())
    kqua = min(x for x in dem if dem[x] == solan)
    return kqua

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    print(trung(a))    