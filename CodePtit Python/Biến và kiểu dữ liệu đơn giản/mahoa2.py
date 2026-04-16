def mahoa2(s,k):
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    a = ""
    for i in range(0,len(s)):
        j = (b.find(s[i]) + k) % len(b)
        a += b[j]
    return a

while True:
    line = input().strip()
    if line == "0":
        break
    k, x = line.split()
    k = int(k)
    y = mahoa2(x, k)
    print(y[::-1])