def ktra(n,a):
    dem = {}
    for i in a :
        if i in dem:
            dem[i] +=1
        else:
            dem[i] = 1
    
    maxdem = max(dem.values())
    if maxdem > n//2 :
        ans = min(x for x in dem if dem[x] == maxdem )
        print(ans) 
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]

    ktra(n,a)