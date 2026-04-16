import math
def ktra(n):
    check = [True] * (n+1)
    check[0]=check[1]= False
    for i in range (2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i,int(n)+1,i):
                check[j] = False
    a = []
    for i in range (1,n+1):
        if check[i]:
            a.append(i)
    return a
a=ktra(10**5)
t=int(input())
for _ in range (t):
    dem=0
    n=int(input())
    for i in range (1,n+1):
        if math.gcd(i,n) == 1:
            dem+=1
    if dem in a:
        print("YES")
    else:
        print("NO")


