def kiemtra(a):
    b = set(a)
    maxa = max(a)
    hople = True
    for i in range(1,maxa):
        if i not in b:
            hople = False
            break

    if hople  == False:
        for i in range(1,maxa):
            if i not in b:
                print(i)
    else:
        print("Excellent!")

n = int(input())
a = []
while len(a) < n:
    a.extend(map(int,input().split()))

kiemtra(a)
