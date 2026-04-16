def chen (s):
    a = ""
    dem=0
    i=len(s)-1
    while i >= 0 :
        if dem < 3:
            a += s[i]
            dem += 1
            i -= 1
        else:
            a += ","
            dem = 0
    return a
s = input()
y = chen(s)
print(y[::-1])