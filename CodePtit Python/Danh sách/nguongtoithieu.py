def ktra(a,k):
    res = []
    for i in range(0, len(a), 2):
        res.append(a[i:i+2])
    dem = {}
    for i in res :
        if len(i) == 2:
            if i in dem :
                dem[i] += 1
            else:
                dem[i] = 1
    demsort = dict(sorted(dem.items()))
    hople = False
    for x in demsort :
        if demsort[x] >= k:
            hople = True
            break
    if hople :
        for x in demsort :
            if demsort[x] >= k:
                print(x,demsort[x])
    else:
        print("NOT FOUND")


n = input().strip()
k = int(input())
ktra(n,k)