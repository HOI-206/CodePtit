def solve(n):
    a = {}
    if len(n) % 2 != 0:
        for i in range(0,len(n)-2,2):
            k = n[i]+n[i+1]
            if k in a :
                a[k] += 1
            else:
                a[k] = 1
    else:
        for i in range(0,len(n)-1,2):
            k = n[i]+n[i+1]
            if k in a :
                a[k] += 1
            else:
                a[k] = 1
    for i in a:
        print(i ,a[i])

n = input()
solve(n)