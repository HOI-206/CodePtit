#________________________________BÀI TẬP CHUẨN BÊN DƯỚI___________________________
"""
import math

n=m=0
a=[0]*1001
b=[0]*1001
ktra = True

def ktra2(a,b,c):
    if math.gcd(a,b) == 1 and math.gcd(a,c) == 1 and math.gcd(b,c) == 1 :
        return True
    else :
        return False

def vao ():
    global n,m,a,b
    n,m = map(int,input().split())
    l = n
    t=0
    while t < (m-n+1):
        b[t] = l
        l+=1
        t+=1
    for i in range (0,3):
        a[i] = i

def ra():
    if (ktra2(b[a[0]], b[a[1]], b[a[2]])):
        print("(", end="")
        print(b[a[0]], b[a[1]], b[a[2]], sep=", ", end="")
        print(")")
    else :
        return

def sinh ():
    global ktra
    i = 3-1
    while i >= 0 and a[i] == (m-n+1)-3+i :
        i-=1
    if i >= 0 :
        a[i] = a[i]+1
        for j in range (i+1,3):
            a[j] = a[i]+j-i
    else :
        ktra =False

def main():
    vao()
    while ktra:
        ra()
        sinh()
main()
"""


#code chuẩn cho bài tập này :
import math

L, R = map(int, input().split())

for a in range(L, R - 1):
    for b in range(a + 1, R):
        if math.gcd(a, b) != 1:
            continue
        for c in range(b + 1, R + 1):
            if math.gcd(a, c) == 1 and math.gcd(b, c) == 1:
                print(f"({a}, {b}, {c})")
