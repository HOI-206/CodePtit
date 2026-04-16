def ktra(a, b, c):
    i = j = k = 0
    n, m, l = len(a), len(b), len(c)
    res = []

    while i < n and j < m and k < l:
        if a[i] == b[j] == c[k]:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
        else:
            mn = min(a[i], b[j], c[k])
            if a[i] == mn:
                i += 1
            elif b[j] == mn:
                j += 1
            else:
                k += 1

    return res


t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:m]
    c = list(map(int,input().split()))[:k]
    g = ktra(a,b,c)
    if len(g) != 0:
        print(*g)
    else:
        print("NO")