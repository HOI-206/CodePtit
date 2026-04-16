def ktra(a):

    hople = True
    for i in range(0,len(a)):
        if i % 2 == 0:
            if a[i] != a[0]:
                hople = False
                break
        else:
            if a[i] != a[1]:
                hople = False
                break
    if hople :
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    a = input()
    ktra(a)