def ktra (a):
    parts = a.split('.')
    if len(parts) != 4 :
        print("NO")
        return
    for p in parts :
        if not p.isdigit():
            print("NO")
            return
        if len(p) > 1 and p[0] == '0' :
            print("NO")
            return
        x = int(p)
        if x < 0  or x > 255 :
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    s = str(input())
    ktra(s)