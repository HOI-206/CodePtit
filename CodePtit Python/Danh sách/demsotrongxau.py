def dem(n,k):
    dem = 0
    i = 0
    while i + len(k) <= len(n):
        if n[i:i+len(k)] == k :
            dem+=1
            i+=len(k)
        else:
            i+=1
    print(dem)

t = int(input())
for _ in range(t):
    n = input()
    k = input()
    dem(n,k)