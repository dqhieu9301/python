test = int(input())
while test>0:
    n = input()
    res1 = "" + n[0] + n[1]
    res2 = "" + n[len(n)-2] + n[len(n)-1] 
    if res1 == res2: print("YES")
    else: print("NO")
    test -=1
