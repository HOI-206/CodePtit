def  tinh(a,k,n):
    tongtren = 0
    tongduoi = 0
    for i in range(0,n):
        for j in range(0,n):
            if j > i :
                tongtren += a[i][j]
            elif j < i:
                tongduoi += a[i][j]
    l = abs(tongtren - tongduoi)
    if l <= k :
        print("YES")
        print(l)
    else:
        print("NO")
        print(l)


n = int(input())
a = [list(map(int,input().split()))[:n] for _ in range(n)]
k = int(input())

tinh(a,k,n)