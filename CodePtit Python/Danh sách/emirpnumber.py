def snt_making(n):
    a = []
    check = [True] * (n+1)
    check[0] = check[1] = False
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*i,n+1,i):
                check[j] = False

    for i in range(n+1):
        if check[i] :
            a.append(i)
    return a

a = set(snt_making(10**6))

def doixung (n):
    m = str(n)
    if m == m[::-1]:
        return False
    if int(m[::-1]) not in a :
        return False
    return True

def ktra(n):
    c = [0] * n
    b = []
    prime = []
    for i in range(n):
        if i in a :
            prime.append(i)

    for i in prime :
        k = str(i)
        if doixung(i) and c[i] == 0:
            if int(k[::-1]) in prime :
                b.append(i)
                b.append(int(k[::-1]))
                c[i] = c[int(k[::-1])] = 1
    print(*b)

t = int(input())
for _ in range(t):
    n = int(input())
    ktra(n)