from re import M


def Check(n,m):
    for i in range(len(n)):
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(m[i]) - ord(m[i-1])): return False
    return True

test = int(input())
while test>0:
    n = str(input())
    m = ""
    for i in n: m = i + m
    if(Check(n,m) == True): print("YES")
    else: print("NO")
    test -=1