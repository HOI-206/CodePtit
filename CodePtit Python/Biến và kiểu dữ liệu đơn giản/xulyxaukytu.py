def xuly(a,b):
    a = list(set(a))
    b = list(set(b))
    a1 = []
    b1 = []
    for i in a:
        a1.append(i.lower())
    for i in b:
        b1.append(i.lower())
    hop = []
    giao = []
    for i in a1 :
        if i in b1 :
            giao.append(i)
        else :
            hop.append(i)
    for i in b1:
        hop.append(i)
    hop.sort()
    giao.sort()
    print(*hop)
    print(*giao)

a = list(map(str,input().split()))
b = list(map(str,input().split()))
xuly(a,b)