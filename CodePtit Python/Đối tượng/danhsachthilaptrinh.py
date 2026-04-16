def chuanhoa(s):
    return int(s[-1:])
class School:
    def __init__(self,id,team,truong):
        self.id = id
        self.team = team
        self.truong = truong
class Student:
    def __init__(self,ma,ten,mateam):
        self.ma = ma
        self.ten = ten
        self.mateam = mateam

n = int(input())
sch = {}
for i in range(1,n+1):
    id = f"Team{i:02d}"
    team = input()
    truong = input()
    sch[id] = School(id,team,truong)
m = int(input())
ds = []
for i in range(1,m+1):
    ma = f"C0{i:02d}"
    ten = input().strip()
    mateam = input().strip()
    ds.append(Student(ma,ten,mateam))

ds.sort(key = lambda x : x.ten)
for i in ds:
    c = sch[i.mateam]
    print(i.ma ,i.ten ,c.team ,c.truong)