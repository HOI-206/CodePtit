n = int(input())
a = []
for _ in range(n):
    a.append(input().lower())

a = set(a)
print(len(a))