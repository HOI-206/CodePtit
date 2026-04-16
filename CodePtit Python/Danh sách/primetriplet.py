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

def ktra(n):
    dem = 0
    prime = []
    for i in range(n+1):
        if i in a :
            prime.append(i)
    for i in prime:
        if i+2 in a or i+4 in a :
            if i+6 in a and i+6 <= n:
                dem+=1

    print(dem)



t = int(input())
for _ in range(t):
    n = int(input())
    ktra(n)