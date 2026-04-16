def chuanhoa(s):
    return ' '.join(s.split()).title()

class khachhang:
    def __init__(self,ma,ten,loai,dau,cuoi):
        self.ma = ma
        self.ten = chuanhoa(ten)
        self.loai = loai
        self.dau = int(dau) 
        self.cuoi = int(cuoi)
        self.tinh()

    def tinh(self):
        sodien = self.cuoi - self.dau
        if self.loai == "A":
            dinhmuc = 100
        elif self.loai == "B":
            dinhmuc = 500
        elif self.loai == "C":
            dinhmuc = 200

        if sodien < dinhmuc:
            self.duoi = sodien * 450
            self.tren = 0
            self.vat = 0
        else:
            self.duoi = dinhmuc * 450
            self.tren = (sodien - dinhmuc) * 1000
            self.vat = self.tren // 20

        self.total = self.duoi + self.tren + self.vat

n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"KH{i:02d}"
    ten = input().strip()
    loai,dau,cuoi = (input().split())
    ds.append(khachhang(ma,ten,loai,dau,cuoi))
ds.sort(key=lambda x :-x.total)
for i in ds:
    print(i.ma, i.ten, i.duoi, i.tren, i.vat, i.total)
