def ktra(a):
    a = list(set(a))
    a.sort()
    b = a[-1] - a[0] + 1 - len(a)
    return b


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    print(ktra(a))