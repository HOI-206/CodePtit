import math
def ktra(a):
    a = sorted(a)
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if math.gcd(a[i],a[j]) == 1 :
                print(str(a[i]) +" "+str(a[j]))
    


n = int(input())
a = list(map(int,input().split()))[:n]
ktra(a)
