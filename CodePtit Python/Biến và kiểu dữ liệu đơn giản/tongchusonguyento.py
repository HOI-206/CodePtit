def snt_making(n):
    a=[]

    check=[True]*(n+1)
    check[0]=check[1]=False

    for i in range(2 , int(n**0.5)+1):
        if check[i] : 
            for j in range(i*i, n+1 ,i):
                check[j]=False
    
    for i in range(2,n+1):
        if check[i] == True :
            a.append(i)
    
    return a

a = snt_making(10**5)

def check(n):
    tong = 0
    for i in range(0,len(n)):
        tong += int(n[i])
    if tong in a :
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):

    n = str(input())
    check(n)