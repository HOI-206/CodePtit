def ktra(x,m):
    ds = []
    res = ''
    while x > 0:
        ds.append(str(x%m))
        x //= m
    ds.reverse()
    for i in ds:
        res += i
    if res == res[::-1]:
        return True
    else:
        return False

def chuanhoa(a,b,m):
    dem = 0
    check = True
    if m == 2 :
        for i in range(a,b+1):
            if ktra(i,m):
                dem +=1
    else:
        for i in range(a,b+1):
            for j in range(2,m+1):
                if ktra(i,j) == False:
                    check = False
                    break
            if check:
                dem += 1
            check = True
    print(dem)
    

a,b,m = map(int,input().split())
chuanhoa(a,b,m)