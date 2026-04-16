def xuly(a):
    return a.lstrip('0') or '0'


def tong(a,b):
    if len(b) > len(a):
        a,b = b,a
    i=len(a)-1
    j=len(b)-1
    nho = 0
    k = []
    while i >= 0 :
        x = int(a[i]) + nho
        if j >= 0 :
            y = int(b[j])
        else:
            y = 0
        if x + y >= 10:
            k.append(str((x+y)%10))
            nho = 1
        else:
            k.append(str(x+y))
            nho = 0
        i-=1
        j-=1
    if nho == 1:
        k.append('1')
    kqua = ''.join(k[::-1])
    print(xuly(kqua)) 

n = input().strip()
m = input().strip()
tong(n,m)