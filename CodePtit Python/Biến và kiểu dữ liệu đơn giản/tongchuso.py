def thugon(a):
    total = 0
    for ch in a:
        total += int(ch)
    return str(total)

def tinh(a):
    if a[0] == '-':
        a = a[1:]
    if len(a) == 1:
        return 1 
    dem = 0
    while len(a) > 1:
        a = thugon(a)
        dem += 1
    return dem

a = input()
print(tinh(a))