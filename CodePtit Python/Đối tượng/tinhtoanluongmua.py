import math
from decimal import Decimal, ROUND_HALF_UP

class luuluong :
    def __init__(self ,ten ,bdau ,kthuc ,ll ):
        self.ten = ten
        self.bdau = bdau
        self.kthuc = kthuc
        self.ll = ll
    def time (self):
        gio1 = int(self.bdau[:2])
        phut1 = int(self.bdau[3:])
        gio2 = int(self.kthuc[:2])
        phut2 = int(self.kthuc[3:])
        time1 = gio1 * 60 + phut1
        time2 = gio2 * 60 + phut2
        totaltime = time2 - time1
        return totaltime
def tinh(a,b):
    return f"{a*60/b:.02f}"
        

n = int(input())
ds = []
kvuc = {}
for i in range(n):
    ten = input().strip()
    bdau = input()
    kthuc = input()
    ll = int(input())
    ds.append(luuluong(ten,bdau,kthuc,ll))
    if ten in kvuc :
        continue
    else:
        kvuc[ten] = 1
for key in kvuc:
    tongll = tongtg = 0
    for i in ds:
        if i.ten == key :
            tongtg += i.time()
            tongll += i.ll
    kvuc[key] = tinh(tongll,tongtg)
i = 1
for key in kvuc:
    print(f"T{i:02d} {key} {kvuc[key]}")
    i+=1