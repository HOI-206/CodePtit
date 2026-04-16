import math

class Rectangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.valid = x > 0 and y > 0
    def perimeter(self):
        if not self.valid:
            return "INVALID"
        return 2*(self.x + self.y)
    
    def area(self):
        if not self.valid:
            return ""
        return self.x * self.y
    
    def color(self):
        if not self.valid:
            return ""
        return self.z.capitalize()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
