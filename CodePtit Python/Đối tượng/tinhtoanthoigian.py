def chuanhoa (x):
    h , m = map(int, x.split(":"))
    time = h * 60 + m
    return time

class gamer :
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        self.vao = chuanhoa(vao)
        self.ra = chuanhoa(ra)
        self.time = self.ra - self.vao
        h = self.time // 60
        m = self.time % 60
        self.gio = h
        self.phut = m

n = int(input())
ds = []
for i in range(n):
    ma = input().strip()
    ten = input().strip()
    vao = input().strip()
    ra = input().strip()
    ds.append(gamer(ma,ten,vao,ra))
ds.sort(key=lambda x : (-x.time, x.ma))
for i in ds :
    print(i.ma ,i.ten ,i.gio,"gio" ,i.phut ,"phut")