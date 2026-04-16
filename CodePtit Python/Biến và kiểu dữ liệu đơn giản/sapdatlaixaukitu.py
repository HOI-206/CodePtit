def ktra(a,b):
    n = []
    m = []
    for i in a:
        n.append(i)
    for j in b:
        m.append(j)
    n.sort()
    m.sort()
    c = ''.join(n)
    d = ''.join(m)
    if c == d :
        return True
    else:
        return False
    
t = int(input())
for i in range(1,t+1):
    a = str(input().strip())
    b = str(input().strip())
    if ktra(a,b) :
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")