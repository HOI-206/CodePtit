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

b = set(snt_making(501))

def ktra(a):
    prime = ('2','3','5','7')
    hople = True
    for i in range(0,len(a)):
        if i in b and a[i] not in prime:
            hople = False
            break
        elif i not in b and a[i] in prime:
            hople = False
            break
    if hople :
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    a = input()
    ktra(a)