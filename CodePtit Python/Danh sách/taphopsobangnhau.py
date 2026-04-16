def solve(a,b):
    a_set = set(a)
    b_set = set(b)
    d = a_set - b_set
    c = b_set - a_set
    if len(d) == len(c) == 0:
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:m]

solve(a, b)