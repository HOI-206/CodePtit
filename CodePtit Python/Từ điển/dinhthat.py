def matrix(n,m,a):
    s = [[0]*n for _ in range(n)]
    i = 0
    j = 1
    while j < len(a):
        s[a[i]-1][a[j]-1] = 1
        i+=2
        j+=2
    return s

def solve(n,m,u,v):

for _ in range(int(input())):
    n,m,u,v = map(int,input().split())
    a = []
    for i in range(m):
        j1,j2 = map(int,input().split())
        a.append(j1)
        a.append(j2)
    solve(n,m,u,v)
    matrix(n,m,a)