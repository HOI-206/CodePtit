def biendoi (a):
    dem = 0
    while a[0] != a[1] or a[1] != a[2] or a[2] != a[3] :
        b = [0] * 4
        for i in range(0,3):
            b[i] = abs(a[i] - a[i+1])
        b[3] = abs(a[3]-a[0])
        a = b
        dem+=1
    return dem

while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        break
    print(biendoi(a))