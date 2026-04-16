class sv:
    def __init__(self,ten,ac,apply):
        self.ten = ten
        self.ac = ac
        self.apply = apply
n = int(input())
ds = []
for i in range(n):
    ten = input().strip()
    ac ,apply = map(int,input().split())
    ds.append(sv(ten,ac,apply))
ds.sort(key=lambda x : (-x.ac , x.apply))
for i in ds :
    print(i.ten ,i.ac ,i.apply)