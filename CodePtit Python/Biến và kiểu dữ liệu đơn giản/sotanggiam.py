def ktra():
    n= input()
    i=0
    while  i+1 < len(n) :
        if int(n[i]) < int(n[i+1]) :
            i+=1
        else :
            break
    if i == 0 or i == len(n) - 1:
        print("NO")
        return
    hople = True
    for j in range(i,len(n)-1):
        if int(n[j]) <= int(n[j+1]):
            hople=False
    if hople :
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    ktra()