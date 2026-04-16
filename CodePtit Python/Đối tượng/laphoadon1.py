def dongia(n):
    if(n > 100):
        n-= 100
        return 50 * 100 + 50 * 150 + n * 200 
    elif n> 50:
        n-= 50
        return 50*100+n*150
    return n*100

def phukien(n):
    if(n > 100):return 1.05
    elif n > 50:return 1.03
    return 1.02

class kh:
    def __init__(self, ma, ten, old, new):
        self.ma = ma
        self.ten = ten
        n = new - old
        giatri = dongia(n)
        self.giatri = (giatri*phukien(n))


t = int(input())
ds = []
for i in range(1,t+1):
    ma = f"KH{i:02d}"
    ten = input().strip()
    old = int(input())
    new = int(input())
    ds.append(kh(ma, ten, old, new))
ds.sort(key = lambda x:(-x.giatri))

for i in ds:
    print(i.ma, i.ten, f"{i.giatri:.0f}")