def snt(n):
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0 : return False
    return True

def tinh(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    i = 0
    hople = False
    while i < len(b)-1 :
        tong1 = 0
        tong2 = 0
        for j in range(i+1):
            tong1 += b[j]
        if snt(tong1) :
            for j in range(i+1,len(b),1):
                tong2 += b[j]
            if snt(tong2) :
                hople = True
                print(i)
                break
        i += 1
    if hople == False:
        print("NOT FOUND")


n = int(input())
a = list(map(int,input().split()))[:n]
tinh(a)