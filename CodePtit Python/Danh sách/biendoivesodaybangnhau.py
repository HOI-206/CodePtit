def snt_making(n):
    a = []
    check = [True] * (n+1)
    check[0] = check[1] = False
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i,n+1,i):
                check[j] = False
    for i in range(n+1):
        if check[i]:
            a.append(i)

    return a

a = snt_making(10**6)
l = set(a)

def ktra(n):
    indexv = -1
    for i in range(n,2,-1):
        if i in l:
            indexv = a.index(i)
            break
    if indexv != -1:
        c = a[indexv]
        d = a[indexv+1]
        if d - n > n - c :
            return n-c
        elif d - n < n - c :
            return d-n
        else:
            return d-n
def solve(o):
    b = []
    for i in (o):
        if i in l :
            b.append(0)
        else:
            b.append(ktra(i))
    print(max(b))


n = int(input())
o = list(map(int,input().split()))
solve(o)