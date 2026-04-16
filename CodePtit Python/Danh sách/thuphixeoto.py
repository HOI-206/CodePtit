class tram:
    def __init__(self,bien,loaixe,socho,hdong,ngay):
        self.bien = bien
        self.loaixe = loaixe
        self.socho = int(socho)
        self.hdong = hdong
        self.ngay = ngay

    def tinhtien(self):
        tien = 0
        if self.loaixe == 'Xe_con':
            if self.socho == 5 :
                tien = 10000
            elif self.socho == 7 :
                tien = 15000
        elif self.loaixe == 'Xe_tai' :
            tien = 20000
        elif self.loaixe == 'Xe_khach' :
            if self.socho == 29 :
                tien = 50000
            elif self.socho == 45 :
                tien = 70000
        return tien

n = int(input())
ds = []
ngayx = {}
for i in range(n):
    bien, loaixe , socho , hdong , ngay = map(str,input().split())
    ds.append(tram(bien,loaixe,socho,hdong,ngay))
    if ngay in ngayx:
        continue
    else :
        ngayx[ngay] = 1
for key in ngayx:
    tong = 0
    for i in range(n):
        if ds[i].ngay == key and ds[i].hdong == 'IN':  
            tong += ds[i].tinhtien()
    ngayx[key] = tong
for key in ngayx :
    print(key,": ",ngayx[key],sep = '')


    




