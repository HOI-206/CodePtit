import sys
import re
def xuly(a):
    a = ' '.join(a.split()).lower()
    cau = re.split(r'[.!?]',a)
    for i in cau:
        i = i.strip()
        if i:
            print(i.capitalize())

a = sys.stdin.read()
xuly(a)