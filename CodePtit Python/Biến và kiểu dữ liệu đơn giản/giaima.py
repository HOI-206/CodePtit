def giaima(s):
    a=""
    for i in range(1,len(s),2):
        a=a+(s[i-1] * int(s[i]))
    print(a)
t = int(input())
for _ in range(t):
    s=input()
    giaima(s)