import math
from decimal import Decimal
def chuanhoa(x):
    if x > 10 :
        return x / 10
    else:
        return x
class nv :
    def __init__(self, ma, ten, diem1, diem2):
        self.ma = ma
        self.ten = ten
        self.diem1 = chuanhoa(diem1)
        self.diem2 = chuanhoa(diem2)
        trungbinh = (self.diem1 + self.diem2) / 2
        self.tb = trungbinh

    def duyet(self):
        if self.tb > 9.5 :
            return "XUAT SAC"
        elif self.tb >= 8 :
            return "DAT"
        elif self.tb >= 5 :
            return "CAN NHAC"
        else :
            return "TRUOT"          

n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"TS0{i}"
    ten = input().strip()
    diem1 = float(input())
    diem2 = float(input())
    ds.append(nv(ma,ten,diem1,diem2))
ds.sort(key=lambda x : (-x.tb , x.ma))
for i in ds :
    print(i.ma ,i.ten ,f"{i.tb:.2f}" ,i.duyet())