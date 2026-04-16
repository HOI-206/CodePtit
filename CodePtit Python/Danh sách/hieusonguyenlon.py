def xuly(a):
    a = a.lstrip('0')
    return a if a else "0"

def tinhhieu(a, b):
    a = xuly(a)
    b = xuly(b)

    giatriam = False
    if len(a) < len(b) or (len(a) == len(b) and a < b):
        a, b = b, a
        giatriam = True

    i = len(a) - 1
    j = len(b) - 1
    muon = 0
    res = []

    while i >= 0:
        x = int(a[i]) - muon
        if j >= 0:
            y = int(b[j])
        else:
            y = 0

        if x < y:
            x += 10
            muon = 1
        else:
            muon = 0

        res.append(str(x - y))
        i -= 1
        j -= 1

    kqua = xuly(''.join(res[::-1]))

    if giatriam:
        kqua = '-' + kqua
    return kqua

a = str(input())
b = str(input())
print(tinhhieu(a,b))