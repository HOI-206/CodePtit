import sys

def check(a):
    dem = 0 
    for i in range(0,len(a)-1):
        if a[i] != a[i+1]:
            dem +=1
    return dem

t = 1
for _ in range(t):
    n = int(input())
    a = list(map(int,sys.stdin.read().split()))[:n]
    print(check(a))