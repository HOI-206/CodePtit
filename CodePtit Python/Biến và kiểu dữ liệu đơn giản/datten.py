n = k = 0
a = []
chon = []
ktra = True
def vao():
    global n,k,chon,a
    
    n,k = map(int,input().split())
    a = list(map(str,input().split()))[:n]
    a = list(set(a))
    a.sort()
    if len(a) < k : return
    for i in range(k):
        chon.append(i)

def ra():
    b = []
    for i in range(k):
        b.append(a[chon[i]])
    print(*b)

def sinh():
    global ktra
    i = k-1
    while i >= 0 and chon[i] == len(a) - k + i : i-=1
    if i >= 0 :
        chon[i] +=1
        for j in range(i+1,k):
            chon[j] = chon[i]+j-i
    else:
        ktra = False

vao()
while ktra:
    ra()
    sinh()

