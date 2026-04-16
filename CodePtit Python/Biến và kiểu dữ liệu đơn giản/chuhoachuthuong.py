def ktra():
    s = input()
    dem1=0
    dem2=0
    for i in range (0,len(s)):
        if s[i] == s[i].upper() and s[i].isalpha():
            dem2+=1
        else:
            dem1+=1
    if dem1 >= dem2:
        print(s.lower())
    else:
        print(s.upper())
ktra()