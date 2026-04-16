def ktra(x):
    if len(x) < 4:
        print("NO")
        return
    if x[0] == x[len(x)-2] and x[1] == x[len(x)-1]:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range (t):
    n=(input())
    ktra(n)