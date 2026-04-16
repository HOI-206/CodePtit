def kiemtra(s):

    a = []
    if len(s) >= 100 :
        for i in range(0,100):
            a.append(s[i])
        print(*a,sep=" ")
    else :
        print(*s,sep=" ")
t = int(input())
for _ in range(t):
    s = list(map(str,input().split()))
    kiemtra(s)
