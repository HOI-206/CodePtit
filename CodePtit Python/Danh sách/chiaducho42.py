def check(a):
    ktr=[0]*41
    dem = 0
    for i in a :
        if ktr[i % 42] == 0:
            ktr[i % 42] = 1
            dem +=1
    return dem
arr = []
d = 10
while d != 0 :
    a = [int(i) for i in input().split()]
    arr.extend(a)
    d -= len(a)
arr = arr[:10]
print(check(a))