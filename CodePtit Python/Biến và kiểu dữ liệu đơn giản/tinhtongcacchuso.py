import string

def tinh(a):
    total = 0
    b = []
    res = ""
    for i in a :
        if i.isalpha():
            b.append(i)
        else:
            total += int(i)
    
    b.sort()
    for i in b:
        res += i
    res+=str(total)
    return res


t = int(input())
for _ in range(t):
    a=str(input())
    print(tinh(a))
