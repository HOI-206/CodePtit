def thuannghich(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False
def timkiem(a,n,m):
    so = 9
    for i in range(0,n) :
        for j in range(0,m):
            if thuannghich(a[i][j]) and a[i][j] > so:
                so = a[i][j]
    if so == 9:
        print("NOT FOUND")
        return 
    else:
        print(so)
        for i in range(0,n) :
            for j in range(0,m):
                if a[i][j] == so:
                    print(f"Vi tri [{i}][{j}]")


n,m = map(int,input().split())
a = [list(map(int,input().split()))[:m] for _ in range(n)]
timkiem(a,n,m)