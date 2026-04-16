n = 0
a = []
ktra = True
kqua = []
dem = 0
def vao():
    global n,a,ktra,kqua,dem
    
    dem = 0
    a.clear()
    kqua.clear()
    n = int(input())
    for i in range(1,n+1):
        a.append(i)
    ktra = True

def ra():
    global dem,kqua

    res = ''
    for i in a:
        res += str(i)
    dem += 1
    kqua.append(res)

def hoanvi():
    global ktra

    i = n-1
    while i > 0 and a[i-1] > a[i]:
        i-=1
    if i > 0 :
        k = n-1
        while a[i-1] > a[k] :
            k-=1
        a[i-1],a[k] = a[k],a[i-1]
        l = i
        r = n-1
        while l <= r :
            a[l],a[r] = a[r],a[l]
            l+=1
            r-=1
    else:
        ktra = False

for _ in range(int(input())):
    vao()
    while ktra == True:
        ra()
        hoanvi()
    print(dem)
    kqua = kqua[::-1]
    print(*kqua,sep=' ')