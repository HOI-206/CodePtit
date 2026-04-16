def check(n):
    a = n[0]
    if len(n) % 2 == 0 or n[0] == n[1] or n[-1] != a:
        return False
    
    for i in range(0,len(n),2):
        if n[i] != a :
           return False
    return True

t = int(input())
for _ in range(t):
    n = str(input())
    if check(n) :
        print("YES")
    else:
        print("NO")