import math
def tinh(a,b):
    print(math.gcd(int(a),int(b)))

t = int(input())
for _ in range(t):
    a = input()
    b =input()
    tinh(a,b)