def solve(a):
    while len(a) > 1:
        n = len(a) // 2
        so1 = a[0:n]
        so2 = a[n:]
        a = str(int(so1) + int(so2))
        print(a)

n = input()
solve(n)