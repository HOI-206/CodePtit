def ktra(a):
    b = {}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    for i in b :
        if b[i] % 2 == 1:
            print(i)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    ktra(a)
