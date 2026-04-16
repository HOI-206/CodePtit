import math

def nguyento():
    count = 0
    n,k = map(int,input().split())
    if n <= 10 or n > 100000 or k <= 1 or k >= 6 :
        return
    for i in range(int(10**(k-1)), int(10**k),1):
        if math.gcd(n,i) == 1:
            print(i, end=' ')
            count += 1
        if count % 10 == 0:
            print()
nguyento()