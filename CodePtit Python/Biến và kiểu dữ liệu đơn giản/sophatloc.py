t = int(input())
for _ in range(t):
    s = input()
    if len(s) >= 2 and s[-2] == '8' and s[-1] == '6':
        print("YES")
    else :
        print("NO")