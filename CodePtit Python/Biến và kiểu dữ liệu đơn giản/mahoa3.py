import string

def xoay(s):
    tong = 0
    a = list(string.ascii_uppercase)
    for i in range(len(s)):
            tong += a.index(s[i])
    step = tong % 26
    ss = ""
    for i in s :
        vtri = a.index(i)
        if vtri + step >= 26 :
            ss += a[vtri + step - 26]
        else:
            ss += a[vtri + step]
    return ss

def tron(a,b):
    ss = ""
    w = list(string.ascii_uppercase)
    for i in range(len(a)):
        o = w.index(a[i])
        e = w.index(b[i])
        if o + e >= 26:
            ss += w[o + e - 26]
        else:
            ss += w[o + e]
    print(ss)

def chia (s):
    a = s[0:len(s) // 2]
    b = s[len(s) // 2:]
    c = xoay(a)
    d = xoay(b)
    tron(c,d)

def tron(a,b):
    ss = ""
    w = list(string.ascii_uppercase)
    for i in range(len(a)):
        o = w.index(a[i])
        e = w.index(b[i])
        if o + e >= 26:
            ss += w[o + e - 26]
        else:
            ss += w[o + e]
    print(ss) 

t = int(input())
for _ in range(t):
    s = input()
    chia(s)

