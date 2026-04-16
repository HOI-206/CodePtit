def trungbinh(a):
    a = sorted(a)
    maxv = a[-1]
    minv = a[0]
    check = [0] * (len(a)+1)
    for i in range(0,len(a)):
        if a[i] == maxv or a[i] == minv :
            check[i] = 1
    tong = 0
    dem = 0
    for i in range(0,len(a)) :
        if check[i] == 0:
            tong += a[i]
            dem +=1
    tong /= dem
    return tong
    

n = int(input())
a = list(map(float,input().split()))[:n]
print(f"{trungbinh(a):.2f}")