def ktra (s):
    i=0
    hople = True
    while i < len(s) :
        if s[i] != '0' and s[i] != '1' and s[i] != '2' :
            hople = False
        i+=1
    if hople :
        print("YES")
    else :
        print("NO")
t= int(input())
for _ in range(t):
    s = input('')
    ktra(s)