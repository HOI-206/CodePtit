def ktra(a):
    a = list(sorted(a))
    i = 0
    while i < len(a)-1 :
        if a[i+1] - a[i] != 1 :
            return a[i] +1
        i+=1
    return a[-1] + 1


n = int(input())
a = list(map(int,input().split()))[:n]
print(ktra(a))