import math
snt = []
def taochuoi(x):
    check = [True] * (x+1)
    check[0]=check[1]=False
    for i in range (2,int(x**0.5)+1):
        if check[i] :
            for j in range(i*i,int(x)+1,i):
                check[j]=False
    for i in range (2,int(x)+1):
        if check[i]:
            snt.append(i)
taochuoi(10**6)
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c=math.gcd(a,b)
    tong = 0
    while c > 0 :
        tong += c%10
        c//=10
    if tong in snt:
        print("YES")
    else :
        print("NO")