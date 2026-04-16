import math
from decimal import Decimal, ROUND_HALF_UP
class sv:
    def __init__(self,ma,ten,diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
        tong = ((diem[0]) * 2) + ((diem[1]) * 2)
        for i in range(2,10):
            tong += (diem[i])
        self.tb = (tong / Decimal("12")).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    def xeploai(self):
        if self.tb >= 9 :
            return "XUAT SAC"
        elif self.tb >= 8 :
            return "GIOI"
        elif self.tb >= 7 :
            return "KHA"
        elif self.tb >= 5 :
            return "TB"
        else:
            return "YEU"

n = int(input())
ds = []
for i in range(1,n+1):
    ten = input().strip()
    diem = list(map(Decimal,input().split()))
    ma = f"HS{i:02d}"
    ds.append(sv(ma,ten,diem))
ds.sort(key=lambda x : (-x.tb , x.ma))
for i in ds :
    print(i.ma, i.ten , f"{i.tb:.1f}", i.xeploai())
