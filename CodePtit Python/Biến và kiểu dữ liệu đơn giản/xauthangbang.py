def  ktra (s) :
    n = s[::-1]
    hople = True
    for i in range (1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(n[i])-ord(n[i-1])) :
            hople = False
            break
    if hople :
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range (t):
    n = str(input())
    ktra(n)
