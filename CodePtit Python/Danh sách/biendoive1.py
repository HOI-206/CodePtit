def dem(n):
    check = [0] * (10**6)
    a = []
    if n == 1 :
        return 1
    else :
        while n != 1:
            if n % 2 == 0 :
                n //= 2
                if check[n] != 1:
                    a.append(n)
                    check[n] = 1
            else:
                n = n*3 + 1
                if check[n] != 1:
                    a.append(n)
                    check[n] = 1
        a.append(1)
        return len(a)

while True:
    n = int(input())
    if n == 0 :
        break
    print(dem(n))
        