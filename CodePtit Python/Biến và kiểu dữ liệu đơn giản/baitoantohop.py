n = k = 0
ktra = True
a = []
b = []
def vao ():
    global n, k, a,ktra

    n, k = map(int,input().split())

# set : chỉ loại trùng , ko sắp xếp 
# sắp xếp name.sort() hoặc b = sorted(a)
    a = list(sorted(set(map(int,input().split()))))

    n=len(a)
    b.clear()
    for j in range(0,k):
        b.append(j+1)
    
    ktra=True

def ra ():

    for i in range(0,k):
        print(a[b[i]-1] , end=' ')
    print()

def sinh ():

    global ktra

    i = k-1
    while i >= 0 and b[i] == n-k+i+1 :
        i-=1
    if i >= 0 :
        b[i] = b[i]+1
        for j in range(i+1,k):
            b[j] = b[j-1] + 1
    else:
        ktra = False

vao()
while(ktra):
    ra()
    sinh()


    


        