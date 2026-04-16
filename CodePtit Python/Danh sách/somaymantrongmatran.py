def timkiem(a,n,m):
    somax = max(max(hang) for hang in a)
    somin = min(min(hang) for hang in a)
    luckynum = somax - somin
    hople = False
    for i in range(0,n) :
        for j in range(0,m):
            if a[i][j] == luckynum :
                hople = True
                break
    if hople:
        print(luckynum)
        for i in range(0,n) :
            for j in range(0,m):
                if a[i][j] == luckynum:
                    print(f"Vi tri [{i}][{j}]")

    else:
        print("NOT FOUND")


n,m = map(int,input().split())
a = [list(map(int,input().split()))[:m] for _ in range(n)]
timkiem(a,n,m)