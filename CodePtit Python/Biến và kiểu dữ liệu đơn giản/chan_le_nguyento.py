def snt(n):
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0 :
            return False
    return True

def check (n) :
    for i in range(0,len(n)):
        if i % 2 == 0 :
            if n[i] not in {'0','2','4','6','8'} :
                return False
        else:
            if n[i] not in {'1','3','5','7','9'}:
                return False
    return True

t = int(input())
for _ in range(t):
    n = str(input())
    total = 0
    if check(n) :
        for i in range(len(n)):
            total += int(n[i])
        if snt(total) :
            print("YES")
        else:
            print("NO")
    else :
        print("NO")