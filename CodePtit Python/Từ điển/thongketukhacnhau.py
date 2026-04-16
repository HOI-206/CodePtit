def solution(a):
    w = []
    
    for line in a:
        s = ''
        line = line.lower() + ' '
        
        for ch in line:
            if ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                s += ch
            else:
                if s != '':
                    w.append(s)
                    s = ''
    
    d = {}
    for i in w:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    res = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    
    for i, j in res:
        print(i, j)


n = int(input())
a = []
for _ in range(n):
    a.append(input())

solution(a)