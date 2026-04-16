def giai (a):
    b = a.sort()
    midc = b[ len(b) // 2 ]
    dem1 = 0
    for i in a:
        dem1 += abs( i - midc )
    print(dem1 ,midc)

n = int(input())
a = list(map(int,input().split()))[:n]
giai(a)