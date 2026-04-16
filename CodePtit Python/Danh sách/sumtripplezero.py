def ktra(n,a):
    dem = 0
    tong = 0
    for i in range(0,n-2):
        l = i+1
        r = n-1
        while l < r :
            tong = a[i] + a[l] +a[r]
            if tong == 0 :
                dem +=1 
                l += 1
            elif tong < 0 :
                l+=1
            else :
                r-=1

    print(dem)
            

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(sorted(map(int,input().split())))
    ktra(n,a)