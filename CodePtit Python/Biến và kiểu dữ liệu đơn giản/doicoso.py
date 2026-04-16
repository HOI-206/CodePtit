import string

def coso (n,b):
    res = ""
    a = list(string.ascii_uppercase)
    indexch = []
    for i in range (10,37):
        indexch.append(i)
    if b == 2 :
        while n >= b :
            res += str(n % b)
            n //= b
        if n == 1 :
            res += str(1)
        else:
            res += str(0)
    else :
        c = []
        while n >= b :
            if n % b >= 10 :
                res += str(a[indexch.index(n % b)])
                n //= b
            else :
                res += str(n % b)
                n //= b 
        if n >= 10:
            res += a[indexch.index(n)]
        else:
            res += str(n)
    return res[::-1]

t = int(input())
for _ in range(t):
    n , b = map(int,input().split())
    print(coso(n,b))