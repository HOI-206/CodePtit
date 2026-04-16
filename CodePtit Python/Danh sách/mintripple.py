def tinh_3_min(a):
    INF = 10**18
    x1 = x2 = x3 = INF

    for i in a:
        if i <= x1:
            x3 = x2
            x2 = x1
            x1 = i
        elif i <= x2:
            x3 = x2
            x2 = i
        elif i < x3:
            x3 = i

    return x1 + x2 + x3


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(tinh_3_min(a))