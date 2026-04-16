class toado:
    def __init__(self,dau,cuoi):
        self.dau = dau
        self.cuoi = cuoi

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        dau,cuoi = map(int,input().split())
        a.append(toado(dau,cuoi))
    a.sort(key = lambda x : (x.cuoi , x.dau))
    dem = 1
    ind = 0
    for i in range(1,n):
        if a[i].dau >= a[ind].cuoi:
            dem += 1
            ind = i
    print(dem)
        