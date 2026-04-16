def snt_making(n):
    a = []
    check = [1] * (n+1)
    check[0]=check[1]=0
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for i in range(i*i,n+1,i):
                check[i]=0
    for i in range(n+1):
        if check[i]:
            a.append(i)
    return a

snt = snt_making(10**4)

def  ktra(a):
    c = []
    b = [0]*len(a)
    for i in range (len(a)):
        if a[i] in snt:
            b[i] = 1
            c.append(a[i])
    c.sort()
    d = []
    k = 0
    for i in range(len(a)):
        if b[i] == 0:
            d.append(a[i])
        else:
            d.append(c[k])
            k+=1
    print(*d)

n = int(input())
a = list(map(int,input().split()))
ktra(a)