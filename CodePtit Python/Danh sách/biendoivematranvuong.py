def biendoi(a, n, m):
    d = []

    if n > m:
        loai = n - m
        da_loai = 0
        for i in range(n):
            if i % 2 == 0 and da_loai < loai: 
                da_loai += 1
                continue
            row = []
            for j in range(m):
                row.append(a[i][j])
            d.append(row)
    else:
        loai = m - n          # số cột cần loại
        for i in range(n):
            row = []
            da_loai = 0
            for j in range(m):
                if j % 2 == 1 and da_loai < loai: 
                    da_loai += 1
                    continue
                row.append(a[i][j])
            d.append(row)

    for row in d:
        print(*row)


n, m = map(int, input().split())
a = [list(map(int, input().split()))[:m] for _ in range(n)]
biendoi(a, n, m)