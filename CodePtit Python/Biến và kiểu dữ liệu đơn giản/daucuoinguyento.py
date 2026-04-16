def check(n):
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0 : return False
    return True

def check1 (n):
    m = n[:3]
    l = n[-3:]
    if (check(int(m))) and check(int(l)):
        return True
    else :
        return False

t = int(input())
for _ in range(t):
    n = str(input())
    if check1(n) :
        print("YES")
    else :
        print("NO")