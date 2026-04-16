def ktra(n):
    res = []
    nho = 0
    for i in range(len(n)-1,0,-1):
        x = int(n[i]) + nho
        if x >= 5 :
            res.append('0')
            nho = 1
        else:
            res.append('0')
            nho = 0

    if nho == 1 :
        res.append(str(int(n[0]) + 1))
    else:
        res.append(n[0])
    kqua = ''.join(res[::-1])
    print(kqua)



t = int(input())
for _ in range(t):
    n = input()
    ktra(n)