def tinh(a):
    kqua = int(a[0]) * (2**2) + int(a[1]) * (2**1) + int(a[2]) * (2**0)
    return str(kqua)

def chia(a):
    b = []
    if len(a) % 3 == 0 :
        for i in range(0,len(a),3):
            b.append(a[i:i+3])
    else:
        while len(a) % 3 != 0:
            a = '0' + a
        for i in range(0,len(a),3):
            b.append(a[i:i+3])

    res= ""
    for i in b :
        res += tinh(i)

    print(res)

n = input()
chia(n)