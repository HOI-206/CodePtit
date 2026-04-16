def tach(a,k):
    b = list(sorted(a))
    dem = 0
    res = ''
    for i in range(0,len(b)-1):
        if b[i+1]-b[i] <= k :
            res += str(b[i])
        else :
            res = ''
            dem +=1
    dem += 1
    print(dem)

n,k = map(int,input().split())
a = list(map(int,input().split()))[:n]
tach(a,k)