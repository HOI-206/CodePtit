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

t = int(input())
for _ in range(t):

    s = str(input())
    """
    cách này có thể gây ra lỗi nếu như độ dài nhỏ hơn 4
    y = s[-4] + s[-3] + s[-2] + s[-1]
    """
    y = int(s[-4:])

    if int(y) in a :
        print("YES")
    else:
        print("NO")