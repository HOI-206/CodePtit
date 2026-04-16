def run(ngay,thang):
    if thang == 1:
        return "Ma Ket" if ngay <= 19 else "Bao Binh"
    elif thang == 2:
        return "Bao Binh" if ngay <= 18 else "Song Ngu"
    elif thang == 3:
        return "Song Ngu" if ngay <= 20 else "Bach Duong"
    elif thang == 4:
        return "Bach Duong" if ngay <= 19 else "Kim Nguu"
    elif thang == 5:
        return "Kim Nguu" if ngay <= 20 else "Song Tu"
    elif thang == 6:
        return "Song Tu" if ngay <= 20 else "Cu Giai"
    elif thang == 7:
        return "Cu Giai" if ngay <= 22 else "Su Tu"
    elif thang == 8:
        return "Su Tu" if ngay <= 22 else "Xu Nu"
    elif thang == 9:
        return "Xu Nu" if ngay <= 22 else "Thien Binh"
    elif thang == 10:
        return "Thien Binh" if ngay <= 22 else "Thien Yet"
    elif thang == 11:
        return "Thien Yet" if ngay <= 22 else "Nhan Ma"
    elif thang == 12:
        return "Nhan Ma" if ngay <= 21 else "Ma Ket"

t = int(input())
for _ in range(t):
    ngay, thang = map(int, input().split())
    print(run(ngay, thang))