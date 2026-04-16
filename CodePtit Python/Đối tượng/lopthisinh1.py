import math
from decimal import Decimal

class sv :
    def __init__(self,ten,date,sub1,sub2,sub3):
        self.ten = ten
        self.date = date
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3    
    def tong (self):
        total = self.sub1 + self.sub2 + self.sub3
        print(f"{self.ten} {self.date} {total:.1f}")

ten = input()
date = input()
sub1 = float(input())
sub2 = float(input())
sub3 = float(input())
sv1 = sv(ten,date,Decimal(sub1),Decimal(sub2),Decimal(sub3))
sv1.tong()    