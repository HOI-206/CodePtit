def check(n):
    if n <= 1 : return False
    if n == 2 : return True
    if n % 2 == 0 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0 : return False
    return True

def check1(n):
    dem = 0
    if check(len(n)) == False:
        print("NO")
        return
    else :
        for i in range(0,len(n)):
            if n[i] in {'2','3','5','7'} :
                dem +=1
    if dem > len(n) - dem :
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = str(input())
    check1(n)