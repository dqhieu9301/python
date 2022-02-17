
test = int(input())
while test>0:
    n = str(input())
    res = ""
    res += n[len(n)-2] + n[len(n)-1]
    if int(res) == 86: print("YES")
    else: print("NO")
    test -=1