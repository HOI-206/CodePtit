def solve(n):
    b = [0] * 100
    a = []
    if len(n) % 2 != 0:
        for i in range(0,len(n)-2,2):
            k = int(n[i]+n[i+1])
            if b[k] == 0:
                a.append(k)
                b[k] = 1
    else:
        for i in range(0,len(n)-1,2):
            k = int(n[i]+n[i+1])
            if b[k] == 0:
                a.append(k)
                b[k] = 1
    a = sorted(a)
    print(*a)

n = input()
solve(n)