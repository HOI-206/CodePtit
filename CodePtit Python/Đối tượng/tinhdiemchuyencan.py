class sinhvien:
    def __init__(self,ma,ten,lop):
        self.ma = ma
        self.ten = ten 
        self.lop = lop
class chuyencan:
    def __init__(self,ma,chuoi):
        self.ma = ma
        self.chuoi = chuoi
    def dieukien(self):
        demmuon = 0
        demvang = 0
        for i in self.chuoi :
            if i == 'm':
                demmuon += 1
            elif i == 'v':
                demvang += 1
        kqua = 10 - (demmuon * 1) - (demvang * 2)
        if kqua <= 0 :
            print(0 ,'KDDK')
        else:
            print(kqua)

n = int(input())
ds = []
for i in range(n):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    ds.append(sinhvien(ma,ten,lop))
chuoix = {}
for i in range(n):
    ma , chuoi = map(str,input().split())
    chuoix[ma] = chuyencan(ma,chuoi)
for i in ds:
    c = chuoix[i.ma]
    print(i.ma ,i.ten ,i.lop ,end = ' ')
    c.dieukien()
            