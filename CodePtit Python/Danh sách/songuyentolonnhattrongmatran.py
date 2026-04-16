def snt_making(n):
    a = []
    check = [True] * (n+1)
    check[0] = check[1] = False
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i,n+1,i):
                check[j] = False

    for i in range(n+1):
        if check[i] :
            a.append(i)
    return a

b = set(snt_making(10**3))

def timkiem(a,n,m):
    sntmax = -1
    for i in range(0,n) :
        for j in range(0,m):
            if a[i][j] in b and a[i][j] > sntmax:
                sntmax = a[i][j]
    if sntmax == -1:
        print("NOT FOUND")
        return 
    else:
        print(sntmax)
        for i in range(0,n) :
            for j in range(0,m):
                if a[i][j] == sntmax:
                    print(f"Vi tri [{i}][{j}]")


n,m = map(int,input().split())
a = [list(map(int,input().split()))[:m] for _ in range(n)]
timkiem(a,n,m)