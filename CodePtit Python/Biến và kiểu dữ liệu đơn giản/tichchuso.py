def check(n):
    tich = 1
    for i in range(0,len(n)):
        if n[i] != '0' :
            tich *= int(n[i])
    print(tich)

t = int(input())
for _ in range(t):

    n = str(input())
    check(n)