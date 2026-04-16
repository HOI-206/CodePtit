def snt_making(n):
    a=[]
    check=[True] * (n+1)
    check[0]=check[1]=False

    for i in range(2,int(n**0.5)+1):
        if check[i] :
            for j in range(i*i,n+1,i):
                check[j] = False
    for i in range(n+1):
        if check[i]:
            a.append(i)

    return a

a = snt_making(2*(10**6))

def phantich(n):
    tong = 0
    tmp = n

    for i in a :
        if i * i > tmp:
            break
        dem = 0
        while tmp % i == 0 :
            dem+=1
            tmp//=i
        if dem > 0 :
            tong += dem * i
            dem = 0
    if tmp > 1 :
        tong += tmp

    return tong

def solution(b):
    total = 0
    for i in b:
        total += phantich(i)

    print(total)

t = 1
for _ in range(t):
    n = int(input())
    b=[]
    for i in range(n):
        x = int(input())
        b.append(x)
    solution(b)

    