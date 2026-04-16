def giaithua(n):
    tich = 1
    for i in range(1,n+1):
        tich *= i
    return tich

def tinhtong(n):
    k = int(n)
    tong = 0
    for i in range(len(n)):
        tong += giaithua(int(n[i]))

    if tong == k:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    n = input()
    tinhtong(n)