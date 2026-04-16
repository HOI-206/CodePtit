import sys

def ktra(a):
    dem = 0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                dem += 1

    return dem

input()
a = list(map(int,input().split()))
print(ktra(a))