"""def chuanhoa(x,y):
    a = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    ngay1 , thang1 , nam1 = map(int,x.split("/"))
    ngay2 , thang2 , nam2 = map(int,y.split("/"))
    tongngay = 0
    if nam2 > nam1 :
        for i in range(0,thang2):
            tongngay += a[i]
        if thang1 != 12 :
            for i in range(thang1+1,13):
                tongngay += a[i]
        if nam2 - nam1 > 1:     
            tongngay += (nam2 - nam1 -1) * 365 + ngay2 + (a[thang1] - ngay1) + 1 
        else:
            tongngay += ngay2 + (a[thang1] - ngay1) + 1
    else:
        if thang2 - thang1 > 1:
            for i in range(thang1+1,thang2):
                tongngay += a[i]
            tongngay += ngay2 + (a[thang1] - ngay1) + 1
        elif thang2 - thang1 == 1:
            tongngay = a[thang1] - ngay1 + ngay2 + 1
        else:
            tongngay = ngay2 - ngay1 + 1
    return tongngay
"""
from datetime import datetime

def chuanhoa(x, y):
    d1 = datetime.strptime(x, "%d/%m/%Y")
    d2 = datetime.strptime(y, "%d/%m/%Y")
    return (d2 - d1).days + 1
def phanloai(x):
    a = [0,25,34,50,80]
    return a[int(x[0])]
    
class guest:
    def __init__(self,ma,ten,num,vao,ra,them):
        self.ma = ma
        self.ten = ten
        self.num = num
        self.vao = vao
        self.ra = ra
        self.them = them
        self.tongngay = chuanhoa(self.vao,self.ra)
        self.tien = phanloai(self.num) * self.tongngay + self.them

n = int(input())
ds = []
for i in range(1,n+1):
    ma = f"KH{i:02d}"
    ten = input().strip()
    num = input().strip()
    vao = input().strip()
    ra = input().strip()
    them = int(input())
    ds.append(guest(ma,ten,num,vao,ra,them))
ds.sort(key=lambda x : (-x.tien , x.ma))
for i in ds:
    print(i.ma ,i.ten ,i.num ,i.tongngay ,f"{i.tien}")
