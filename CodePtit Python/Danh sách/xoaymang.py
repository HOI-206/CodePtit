def xoay(a,k):
    dau = a[:k]
    cuoi = a[k:]
    res = cuoi + dau
    print(*res)

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    xoay(a,k)