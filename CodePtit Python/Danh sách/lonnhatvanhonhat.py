def ktra(a):
    b = []
    for i in range(0,len(a)):
        b.append(int(a[i]))
    c = list(set(b))
    if len(c) == 1:
        print("BANG NHAU")
        return
    maxvalue = max(b)
    minvalue = min(b)
    print(minvalue ,maxvalue)



while True:
    n = int(input())
    if n == 0 :
        break
    a = []
    while len(a) < n:
        a.append(input())
    ktra(a)