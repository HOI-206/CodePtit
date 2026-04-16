import string
def ktra(n,k):
    res = ""
    alpha = string.ascii_uppercase
    a = list(alpha)
    i = 0
    while n > 0 :
        res = res + a[i] + res
        i+=1
        n-=1
    return res[k-1]

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    print(ktra(n,k))