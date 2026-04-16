import math
import string

def tinh(a):
    tong = 0
    k = len(a)-1
    i=0
    c = string.ascii_uppercase
    d = list(c)
    while k >= 0 :
        n = int(a[i]) * (2**k)
        tong += n
        i+=1
        k-=1
    if tong >= 10 :
        return d[tong-10]
    else:
        return str(tong)

def chia(a,k):
    res = ""
    while len(a) % k != 0 :
        a = '0' + a
    for i in range(0,len(a),k):
        res += tinh((a[i:i+k]))
    print(res)

t = int(input())
for _ in range(t):
    b = int(input())
    k = int(math.log2(b))
    a = input()
    chia(a,k)