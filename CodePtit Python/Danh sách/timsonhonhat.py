import sys

data = sys.stdin.read().split()
it = iter(data)

t = int(next(it))
INF = 10**18

out = []

for _ in range(t):
    n = int(next(it))

    x1 = x2 = x3 = INF

    for _ in range(n):
        i = int(next(it))
        if i <= x1:
            x3 = x2
            x2 = x1
            x1 = i
        elif i <= x2:
            x3 = x2
            x2 = i
        elif i < x3:
            x3 = i

    out.append(str(x1 + x2 + x3))

sys.stdout.write("\n".join(out))
