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

a = snt_making(10**3)

def ktra (n):
    dem = 0
    if len(n) not in a :
        return
    for i in range(0,len(n)):
        if n[i] == '2' or n[i] == '3' or n[i] == '5' or n[i] == '7' :
            dem+=1
    if dem > len(n) - dem :
        return True
    else:
        return False

t = int(input())
for _ in range(t):

    s = str(input())
    if ktra(s) :
        print("YES")
    else:
        print("NO")