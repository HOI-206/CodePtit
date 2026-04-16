import math

class sophuc:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculator1(self,d2):
        thuctong = self.x + d2.x
        aotong = self.y + d2.y
        thuc = (thuctong*self.x) - (aotong*self.y)
        ao = (thuctong*self.y) + (aotong*self.x)
        return f"{thuc} + {ao}i"

    def calculator2(self,d2):
        thuctong = self.x + d2.x
        aotong = self.y + d2.y
        thuc = thuctong**2 - aotong**2
        ao = 2*thuctong*aotong
        return f"{thuc} + {ao}i"
        
t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))[:4]
    d1 = sophuc(a[0],a[1])
    d2 = sophuc(a[2],a[3])

    kq1 = d1.calculator1(d2)
    kq2 = d1.calculator2(d2)

    print(f"{kq1}, {kq2}")
