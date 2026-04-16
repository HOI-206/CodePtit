import math
def ktra(s) :
    tong = 0
    for i in range(len(s)-1,0,-1):
        if abs(int(s[i]) - int (s[i-1])) != 2:
            print("NO")
            return
        tong += int(s[i])
    tong += int(s[0])
    if tong % 10 == 0 :
        print("YES")
    else :
        print("NO")
t = int(input())
for _ in range(t):
    s = input()
    ktra(s)