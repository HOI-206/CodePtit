class customer :
    def __init__(self,ma,ten,soluong,gia,chietkhau):
        self.ma = ma
        self.ten = ten
        self.soluong = soluong
        self.gia = gia
        self.chietkhau = chietkhau
    def bill (self):
        tong = self.gia * self.soluong - self.chietkhau
        return tong


n = int(input())
ds = []
for i in range(n):
    ma = input().strip()
    ten = input().strip()
    soluong = int(input())
    gia = int(input())
    chietkhau = int(input())
    ds.append(customer(ma,ten,soluong,gia,chietkhau))
ds.sort(key=lambda x : (-x.bill(), x.ma))
for i in ds:
    print(i.ma ,i.ten ,i.soluong ,i.gia ,i.chietkhau ,i.bill())
