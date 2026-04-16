def snt (n) :
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0 : return False
    return True

def ktra(n):
    m = str(n)
    k = n
    b = int(m[::-1])
    total = 0
    while k > 0 :
        total += k % 10
        k //= 10
    if snt(n) and snt (b) and snt(total):
        for i in range(len(m)):
            if m[i] not in ('2','3','5','7') :
                return False
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    if ktra(n):
        print("Yes")
    else:
        print("No")