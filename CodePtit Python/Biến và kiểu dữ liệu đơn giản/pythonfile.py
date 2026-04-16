import string

def ktra (s):
    
    if len(s) < 3 :
        print ("no")
        return 
        
    a = list(string.ascii_lowercase)
    b = list(string.ascii_uppercase)
    c = ['_'] # list , khác với {...} :set
#    d = ['1','2','3','4','5','6','7','8','9']
    condition = a + b + c 

    if not s.endswith(".py"):
        print("no")
        return
    
    name = s[:-3]
    for ch in name:
        if ch not in condition :
            print("no")
            return
        
    print("yes")

s = str(input().lower())
ktra(s)