def tinh():
    n=str(input())
    m=n
    hople = False
    for i in range (1,1001):
        if int(m) % 7 == 0 :
            hople=True
            break
        else :
            k = int(m)
            j = int(m[::-1])
            m = str(k+j)
    if(hople):
        print(m)
    else:
        print("-1")
t = int(input())
for _ in range(t):
    tinh()
