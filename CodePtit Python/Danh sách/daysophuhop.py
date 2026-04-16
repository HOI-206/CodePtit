def check(a, b):
    if len(a) != len(b):
        print("NO")
        return

    a.sort()
    b.sort()

    for i in range(len(a)):
        if a[i] > b[i]:
            print("NO")
            return

    print("YES")
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    check(a, b)
