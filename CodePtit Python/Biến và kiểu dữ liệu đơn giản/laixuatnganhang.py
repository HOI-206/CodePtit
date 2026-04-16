import math
def tinhnam (a,b,c):
    nam = math.log(c/a) / math.log(1+b/100)
    print(math.ceil(nam))
t = int(input())
for _ in range (t):
    n,x,m = map(float,input().split())
    tinhnam(n,x,m)