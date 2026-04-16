def ktra(x):
    #x = input()
    dem = 0
    for i in range (0,len(x)):
        if int(x[i]) == 4 or int(x[i]) == 7:
            dem+=1
    if dem == 4 or dem == 7:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range (t):
    x = input()
    ktra(x)