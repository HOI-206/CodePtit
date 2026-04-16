def ktra (a):
    if a[0] == '8':
        return False
    for i in a :
        if i != '6' and i != '8' :
            return False
    for i in range(0,len(a)-2):
        if a[i] == a[i+1] == a[i+2] == '8' :
            return False
    return True

s = str(input())
if ktra(s) == True:
    print("YES")
else:
    print("NO")