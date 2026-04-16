import sys 
 
n = str(input().upper())
m = 0
a = []
b = []
ktra = True

def vao ():
    global n,m,a,b,ktra

    m = len(n)
    for ch in n :
        a.append(ch)
    for i in range(0,len(n)):
        b.append(i)

t=[]
def ra():
    tmp = []
    for i in range(m):
        tmp.append(a[b[i]])
    t.append(''.join(tmp))
# ' '.join(tmp) : nghiax là thêm cái dấu chèn bất kỳ nào đó vào giữa những thành phần của tmp

def sinh():
    global ktra

    i = m-2
    while i>=0 and b[i] >= b[i+1]:
        i-=1
    if i >= 0:
        k = m-1
        while b[i] > b[k] :
            k-=1
        b[i], b[k] = b[k], b[i]
        s = i+1
        v = m-1
        while s < v :
            b[s], b[v] = b[v], b[s]
            s+=1
            v-=1
    else:
        ktra = False
    
vao()
while(ktra):
    ra()
    sinh()

sys.stdout.write('\n'.join(t))

