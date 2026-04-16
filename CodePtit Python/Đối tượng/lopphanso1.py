import math

class ps :
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def rutgon(self):
        if self.y == 0:
            return
        chung = math.gcd(self.x,self.y)
        dx = self.x // chung
        dy = self.y // chung
        print(dx,"/",dy,sep='')

a = list(map(int,input().split()))[:2]
p = ps(a[0],a[1])
p.rutgon()