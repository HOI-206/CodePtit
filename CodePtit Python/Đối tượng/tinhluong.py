na = [0]*100
nb = [0]*100
nc = [0]*100
nd = [0]*100
for i in range(0,100):
    if i <= 3 :
        na[i] = 10
        nb[i] = 10
        nc[i] = 9
        nd[i] = 8
    elif i >=4 and i<=8 :
        na[i] = 12
        nb[i] = 11
        nc[i] = 10
        nd[i] = 9
    elif i>= 9 and i<=15 :
        na[i] = 14
        nb[i] = 13
        nc[i] = 12
        nd[i] = 11
    elif i>16 :
        na[i] = 20
        nb[i] = 16
        nc[i] = 14
        nd[i] = 13

class nhanvien :
    def __init__(self,ma,ten,luongcb,ngaylam,ban):
        self.ma = ma
        self.ten = ten
        self.luongcb = luongcb
        self.ngaylam = ngaylam
        self.ban = ban

    def tinhluong(self):
        heso = 0
        if self.ma[0] == 'A':
            indx = int(self.ma[1:3])
            heso = na[indx]
        elif self.ma[0] == 'B':
            indx = int(self.ma[1:3])
            heso = nb[indx]
        elif self.ma[0] == 'C':
            indx = int(self.ma[1:3])
            heso = nc[indx]
        elif self.ma[0] == 'D':
            indx = int(self.ma[1:3])
            heso = nd[indx]
        return self.luongcb * self.ngaylam * heso * 1000
    
    def tenban(self):
        return phongban[self.ban]
    
n = int(input())
phongban = {}
for i in range(n):
    pb = input()
    c = pb.split()
    mapb = c[0]
    tenp = ""
    for i in range(1,len(c)) :
        tenp += c[i] + " "
    tenp.strip()
    phongban[mapb] = tenp

m = int(input())
ds = []
for i in range(1,m+1):
    ma = input().strip()
    ten = input().strip()
    luongcb = int(input())
    ngaylam = int(input())
    ban = ma[-2:]
    ds.append(nhanvien(ma,ten,luongcb,ngaylam,ban))
for i in ds :
    print(i.ma ,i.ten ,' '.join(i.tenban().split()) ,i.tinhluong())