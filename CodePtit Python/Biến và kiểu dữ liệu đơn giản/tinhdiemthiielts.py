def xuly(n):
    du = n - int(n)
    if du < 0.25 :
        return int(n)
    elif du >= 0.25 and du < 0.75 :
        du = 0.5
        return int(n) + du
    elif du >= 0.75 :
        du = 1.0
        return int(n)+du

def bangdiem(a,b,c,d):
    diem = {}
    for i in range(3,41):
        if i in (3,4):
            diem[i] = 2.5
        elif i in (5,6):
            diem[i] = 3.0
        elif i in (7,8,9):
            diem[i] = 3.5
        elif i in (10,11,12):
            diem[i] = 4.0
        elif i in (13,14,15):
            diem[i] = 4.5
        elif i in (16,17,18,19):
            diem[i] = 5.0
        elif i in (20,21,22):
            diem[i] = 5.5
        elif i in (23,24,25,26):
            diem[i] = 6.0
        elif i in (27,28,29):
            diem[i] = 6.5
        elif i in (30,31,32):
            diem[i] = 7.0
        elif i in (33,34):
            diem[i] = 7.5
        elif i in (35,36):
            diem[i] = 8.0
        elif i in(37,38):
            diem[i] = 8.5
        else :
            diem[i] = 9.0
    diemread = diem[a]
    diemlisten = diem[b]
    kqua = (diemread + diemlisten + c + d) / 4
    return xuly(kqua)



t = int(input())
for _ in range(t):
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = float(c)
    d = float(d)
    k = bangdiem(a,b,c,d)
    print(f"{k:.1f}")
    
