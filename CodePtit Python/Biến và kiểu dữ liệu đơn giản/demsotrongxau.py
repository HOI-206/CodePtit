def chia(s,n):
    ds = []
    indx = 0
    x = len(n)
    indx2 = x
    dem = 0
    while indx < len(s) and indx2 <= len(s):
        if s[indx:indx2] == n :
            dem +=1
            indx = indx2
            indx2 += x
        else:
            indx +=1
            indx2 +=1
    for i in ds :
        if i == n:
            dem+=1
    print(dem)

for _ in range(int(input())):
    s = input()
    n = input()
    chia(s,n)