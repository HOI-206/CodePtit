import math

class ps:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def tong(self,p2):
        if self.y == 0 or p2.y == 0:
            return 
        dx = self.x * p2.y + self.y * p2.x
        dy = self.y * p2.y
        chung = math.gcd(dx,dy)
        dx //= chung
        dy //= chung
        print(dx,"/",dy,sep='')

a = list(map(int,input().split()))[:4]
p1 = ps(a[0],a[1])
p2 = ps(a[2],a[3])
p1.tong(p2)