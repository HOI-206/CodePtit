def phanloai(x):
    if x[0] == 'A':
        return "TOAN"
    elif x[0] == 'B':
        return "LY"
    elif x[0] == 'C':
        return "HOA"
def uutien (x):
    a = [0,2.0,1.5,1.0,0.0]
    return a[int(x[1])]
class teacher :
    def __init__(self,ma,ten,maxet,diemtin,diemmon):
        self.ma = ma
        self.ten = ten
        self.maxet = maxet
        self.diemtin = diemtin
        self.diemmon = diemmon
        self.mon = phanloai(self.maxet)

    def diem (self):
        diemuutien = uutien(self.maxet)
        self.diemtong = self.diemtin * 2 + self.diemmon + diemuutien
        return float(f"{self.diemtong:.1f}")
    def phanloai (self):
        total = self.diem()
        if total >= 18.0 :
            return "TRUNG TUYEN"
        else:
            return "LOAI"


n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"GV{i:02d}"
    ten = input().strip()
    maxet = input().strip()
    diemtin = float(input())
    diemmon = float(input())
    ds.append(teacher(ma,ten,maxet,diemtin,diemmon))
ds.sort(key = lambda x : (-x.diem() , x.ma))
for i in ds :
    print(i.ma ,i.ten ,i.mon ,i.diem() ,i.phanloai())