def distance (s):
    s1=s
    s2=s[::-1]
    hople=True
    for i in range (1,len(s)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])) :
            hople=False
            break
    if hople :
        print("YES")
    else :
        print("NO")
t = int(input())
for _ in range (t):
    s = input()
    distance(s)