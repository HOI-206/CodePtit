def cacso (n):
    l = str(n)
    for i in range(0,len(l)):
        if l[i] != '2' and l[i] != '4' and l[i] != '6' and l[i] != '8' and l[i] != '0':
            return False
    return True

def ktra1(n):
    s = str(n)
    if s == s[::-1] :
        return True
    return False

def ktra (n):
    a=[]
    for i in range(20,n+1,1):
        if len(str(i)) % 2 == 0:
            if  ktra1(i) :
                if cacso(i) :
                    a.append(i)
                else:
                    continue
            else :
                continue
        else :
            continue
    print(*a)

t = int(input())
for _ in range(t):
    n = int(input())
    ktra(n)