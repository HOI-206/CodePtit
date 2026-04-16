def mahoa1 (s):
    a=""
    dem=1
    for i in range (0,len(s)-1):
        if s[i]==s[i+1]:
            dem+=1
        else:
            a += str(dem)+s[i]
            dem=1
    a+=str(dem)+s[-1]
    return a
t = int(input().strip())
for _ in range(t):
    k = input().strip()
    print(mahoa1(k))