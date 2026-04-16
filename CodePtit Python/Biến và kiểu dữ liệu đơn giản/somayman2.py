def ktra (x):
    for i in range (0,len(x)):
        if x[i] != '4' and x[i] != '7' :
            print("NO")
            return
    print("YES")
t = int(input())
for _ in range (t):
    x = str(input())
    ktra(x)