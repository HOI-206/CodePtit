snt=[]
def snt_making (n):
    check = [True] * (n+1)
    check[0]=check[1]=False
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range (i*i,n+1,i):
                check[j]=False
    for i in range (2,n+1):
        if check[i]:
            snt.append(i)
snt_making(10**6)
def phantich (n):
    a="1 * "
    for i in snt:
        if i*i > n:
            break
        dem = 0
        while n % i == 0 :
            dem += 1
            n //= i
        if dem > 0:
            a += str(i) + "^" +str(dem) +" * "
    if n > 1:
        a += str(n) + "^1"
    return a.rstrip(" * ")
t = int(input())
for _ in range(t):
    n=int(input())
    print(phantich(n))
