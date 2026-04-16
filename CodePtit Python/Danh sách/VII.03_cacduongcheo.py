def ra(n):
    a = []
    for i in range(1,n+1):
        a.append(i)
    b = a[::-1]
    c = [[0] * n for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            c[i][j]=abs(i-j)
    for row in c :
        print(*row)

n = int(input())
ra(n)