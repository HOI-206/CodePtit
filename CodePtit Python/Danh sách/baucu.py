def baucu(a,n,m):
    dem = {}
    for i in a :
        if i in dem:
            dem[i] +=1
        else:
            dem[i] = 1
    c = []
    d = []
    for i in dem:
        d.append(dem[i])
    if len(list(set(d))) == 1 :
        print("NONE")
        return
    else:
        phieu = list(set(d))
        phieu.sort(reverse=True)
        hang2 = phieu[1]
        for k,v in dem.items():
            if v == hang2:
                c.append(k)
    print(min(c))

n , m = map(int,input().split())
a = list(map(int,input().split()))[:n]
baucu(a,n,m)