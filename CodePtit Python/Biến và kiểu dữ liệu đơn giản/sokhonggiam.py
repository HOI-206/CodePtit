def ktra (s):
    hople=True
    for i in range (len(s)-1,0,-1):
        if int(s[i]) < int(s[i-1]) :
            print("NO")
            hople=False
            break
    if hople :
        print("YES")
t = int(input())
for _ in range(t):
    s=input()
    ktra(s)