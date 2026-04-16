#_________________CÁCH 1: O(N)_________________
def tinh(a,n):
    b = [0] * n
    b[0] = 1
    for i in range(0,n):
        dem = 1
        j = i - 1
        while j >= 0 and a[j] <= a[i] :
            dem+=b[j]
            j -= b[j]
        b[i] = dem
    print(*b)
#_________________CÁCH 2: O(N**2)______________
"""
def tinh1(a,n):
    dem = 1
    b = []
    b.append(1)
    for i in range(1,n):
        if a[i] > a[i-1] :
            ok = False
            for j in range(i-1,-1,-1):
                if a[j] <= a[i] :
                    dem +=1
                else:
                    b.append(dem)
                    dem = 1
                    ok = True
                    break
            if not ok :
                b.append(dem)
                dem = 1
        else:
            dem = 1
            b.append(dem)

    print(*b)
"""
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    tinh(a,n)