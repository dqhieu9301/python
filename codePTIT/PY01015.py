
test = int(input())
while test>0:
    n = str(input())
    kt = True
    n.strip()
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            print("NO")
            kt = False
            break
    if kt == True: print("YES")
    test -=1