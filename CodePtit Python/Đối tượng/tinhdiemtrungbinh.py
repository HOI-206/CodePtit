from decimal import Decimal , ROUND_HALF_UP
def chuanhoa(s):
    return ' '.join(s.split()).title()
class sv:
    def __init__(self,ma,ten,diem):
        self.ma = ma
        self.ten = chuanhoa(ten)
        self.diem = float((Decimal(diem)/Decimal(8)).quantize(Decimal('0.01'),ROUND_HALF_UP))

n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"SV{i:02d}"
    ten = input().strip()
    a = float(input().strip())
    b = float(input().strip())
    c = float(input().strip())
    diemtong = (a*3) + (b*3) + (c*2)
    ds.append(sv(ma,ten,diemtong))
ds.sort(key=lambda x :(-x.diem , x.ma))
dem = 1
rank = 1
print(ds[0].ma ,ds[0].ten ,f"{ds[0].diem:.2f}" ,rank)
for i in range(1,n):
    if ds[i].diem == ds[i-1].diem :
        print(ds[i].ma ,ds[i].ten ,f"{ds[i].diem:.2f}" , rank)
        dem += 1
    else :
        print(ds[i].ma ,ds[i].ten ,f"{ds[i].diem:.2f}" , rank+dem)
        rank += dem
        dem = 1
