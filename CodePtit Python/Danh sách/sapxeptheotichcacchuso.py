def tinh(n):
    tich = 1
    while n > 0 :
        tich *= (n % 10)
        n //= 10
    return tich

def xep (a):
    a.sort()
    b = []
    for i in a:
        b.append(tinh(i))
    b.sort()
    c = []
    d = [0] * len(a)
    for i in range(0,len(b)) :
        for j in range(0,len(a)):
            if d[j] == 0 :
                if tinh(a[j]) == b[i] :
                    c.append(a[j])
                    d[j] = 1

    print(*c)
    


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]

    xep(a)