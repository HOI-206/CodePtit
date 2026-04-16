a = []
def lietke (y):
    for i in range (10,y):
        x = str(i)
        if len(x) % 2 != 0 :
            continue
        if x != x[::-1]:
            continue

        hople = True
        for j in x :
            if j not in '02468':
                hople =  False
                break
        if hople:
            a.append(x)
        
t = int(input())
for _ in range (t):
    a.clear()
    n = int(input())
    lietke(n)
    print(*a)
