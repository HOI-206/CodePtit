def solve(a, n):
    deg = [0]*n
    
    for i in range(0, len(a), 2):
        u = a[i] - 1
        v = a[i+1] - 1
        deg[u] += 1
        deg[v] += 1
    
    for i in range(n):
        if deg[i] == n-1:
            print("Yes")
            return
    
    print("No")
     
n = int(input())
a = []
for i in range(n-1):
    x,y = map(int,input().split())
    a.append(x)
    a.append(y)
solve(a,n)