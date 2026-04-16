def check (n):
    tong = 0
    for i in range(0,len(n)):
        tong += int(n[i])
    y = str(tong)
    if y == y[::-1] :
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    s = str(input())
    check(s)