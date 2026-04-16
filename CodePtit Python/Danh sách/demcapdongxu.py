import math

def check (a,n):
    total = 0
    for i in range(n):
        dem = 0
        for j in range(n):
            if a[i][j] == 'C' :
                dem += 1
        total += (dem * (dem-1)) // 2
    for j in range(n):
        dem = 0
        for i in range(n):
            if a[i][j] == 'C' :
                dem += 1
        total += (dem * (dem-1)) // 2
    print(total)
    

n = int(input())
a = [list(input().strip()) for _ in range(n)]
check(a,n)