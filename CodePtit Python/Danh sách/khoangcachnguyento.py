def snt_making(n):
    a = []

    check = [1] * (n+1)
    check[0] = check[1] = 0
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i,n+1,i):
                check[j] = 0

    for i in range(2,n+1):
        if check[i] :
            a.append(i)
    
    return a

a = snt_making(10**5)

def kqua (n,x):
    b = []
    i = 0
    b.append(x)
    while i < n:
        y = x + a[i]
        b.append(y)
        x = y
        i+=1

    print(*b)

t = 1
for _ in range(t):
    n , x = map(int,input().split())
    kqua(n,x)