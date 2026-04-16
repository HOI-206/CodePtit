def tongtich(n):
    total = 0
    times = 1
    a= []
    for i in range(0,len(n)):
        if i % 2 == 1 :
            total += int(n[i])
        else:
            a.append(n[i])
    hople = False
    for i in a :
        if i != '0' :
            hople = True
    if hople == True :
        for i in a :
            if i != '0':
                times *= int(i)
    else:
        times = 0
    print(str(total) + ' ' + str(times))
t = int(input())
for _ in range(t):
    n = str(input())
    tongtich(n)
        
            