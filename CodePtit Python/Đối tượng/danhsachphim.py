class Film:
    def __init__(self,ma,loai,ngay,ten,sotap):
        self.ma = ma
        self.loai = int(loai[-1:])
        self.ngay = ngay
        self.ten = ten
        self.sotap = sotap
    def chuanhoa(self):
        day,mon,year = self.ngay.split('/')
        tong = int(day) + (int(mon) * 30) + (int(year) * 365)
        return tong

n , k = map(int,input().split())
ds = []
for i in range(n):
    x = input()
    ds.append(x)
dsp = []
for i in range(1,k+1):
    ma = f"P{i:03d}"
    loai = input().strip()
    ngay = input().strip()
    ten = input().strip()
    sotap = int(input())
    dsp.append(Film(ma,loai,ngay,ten,sotap))
dsp.sort(key=lambda x : (x.chuanhoa() , x.ten , x.sotap))
for i in dsp:
    print(i.ma ,ds[i.loai-1] ,i.ngay ,i.ten ,i.sotap)