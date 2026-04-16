import math
t = int(input())
for _ in range(t):
    n = (input().strip())
    m = n[::-1]
    if math.gcd(int(n),int(m)) == 1 :
        print("YES")
    else :
        print("NO")
        
        