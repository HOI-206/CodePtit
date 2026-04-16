def check(n):
    tong = 0
    for i in range(0,len(n)):
        tong += int(n[i])
    if tong % 3 == 0 :
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):

    n = str(input())
    check(n)