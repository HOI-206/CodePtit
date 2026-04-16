v=[]
def ktra(a,k,n):
    c = n // k
    for i in range (1,c+1):
        if i*k <= a :
            continue
        b = i*k - a
        v.append(b)
t=1
for _ in range(t):
    v.clear()
    a,k,n = map(int,input().split())
    ktra(a,k,n)
    if len(v) == 0:
        print(-1)
    else:
        print(*v)

"""
a,k,n = map(int, input().split())
def kq(a,k,n):
    b=k-(a%k)
    if a >=n or a+b > n:
        print(-1)
        return
    while a+b <= n:
        print(b, end=' ')
        b+=k
kq(a,k,n)
"""