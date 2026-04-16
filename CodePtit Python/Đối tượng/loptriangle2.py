import math

class tg:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,d2):
        dx = self.x - d2.x
        dy = self.y - d2.y
        d = math.sqrt((dx*dx) + (dy*dy))
        return d
    
def dientich(a,b,c):
    d = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
    return d

t = int(input())
arr = []
for _ in range(t):
    arr += list(map(float,input().split()))
i = 0
for _ in range(t):
    d1 = tg(arr[i],arr[i+1])
    d2 = tg(arr[i+2],arr[i+3])
    d3 = tg(arr[i+4],arr[i+5])
    i += 6
    a = d1.distance(d2)
    b = d1.distance(d3)
    c = d2.distance(d3)
    if a + b <= c or a + c <= b or b + c <= a:
        print("INVALID")
        continue
    print(f"{dientich(a,b,c):.2f}")