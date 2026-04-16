def solve(a,n):
    dau = 0
    cuoi = -1
    tongmax = -10**10
    tongtemp = -10**10
    bdau = 0
    for i in range(0,n):
        if tongtemp < 0:
            tongtemp += a[i]
            bdau = i
        else:
            tongtemp += a[i]
        if (tongtemp > tongmax) or (tongtemp == tongmax and bdau < dau):
            tongmax = tongtemp
            dau = bdau
            cuoi = i
        
    print(dau+1 ,cuoi+1 ,tongmax)


n = int(input())
a = list(map(int,input().split()))[:n]
solve(a,n)