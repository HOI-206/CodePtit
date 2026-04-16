def chuanhoa(s):
    return ' '.join(s.split()).title()

class xettuyen:
    def __init__(self,ma,ten,diem,dtoc,kvuc):
        self.ma = ma
        self.ten = chuanhoa(ten)
        self.dtoc = chuanhoa(dtoc)
        self.kvuc = kvuc
        self.diem = diem
    
    def diemtong(self):
        total = self.diem
        if self.kvuc == 1:
            total += 1.5
        elif self.kvuc == 2:
            total += 1
        elif self.kvuc == 3:
            total += 0.0

        if self.dtoc == "Kinh":
            total += 0.0
        else:
            total += 1.5
        
        return total
    
    def xet(self):
        if self.diemtong() >= 20.5:
            return "Do"
        else:
            return "Truot"

n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"TS{i:02d}"
    ten = input().strip()
    diem = float(input())
    dtoc = input()
    kvuc = int(input())
    ds.append(xettuyen(ma,ten,diem,dtoc,kvuc))
ds.sort(key=lambda x :(-x.diemtong(),x.ma))
for i in ds:
    print(i.ma ,i.ten ,f"{i.diemtong():.1f}" ,i.xet())