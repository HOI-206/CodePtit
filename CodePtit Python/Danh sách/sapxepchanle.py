def sx(a):
    chan = []
    le = []

    for x in a:
        if x % 2 == 0:
            chan.append(x)
        else:
            le.append(x)

    chan.sort()
    le.sort(reverse=True)

    i_chan = 0
    i_le = 0
    kq = []

    for x in a:
        if x % 2 == 0:
            kq.append(chan[i_chan])
            i_chan += 1
        else:
            kq.append(le[i_le])
            i_le += 1

    return kq


n = int(input())

a = []
while len(a) < n:
    a.extend(map(int, input().split()))

a = a[:n]

print(*sx(a))