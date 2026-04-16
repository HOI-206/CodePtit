def snt (n):
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def ktra(a):
    dem = {}
    for i in range(0,len(a)):
        if snt(a[i]):
            if a[i] in dem:
                dem[a[i]] += 1
            else:
                dem[a[i]] = 1
    for k,v in dem.items():
        print(k, v)
            

n = int(input())
a = list(map(int,input().split()))[:n]
ktra(a)