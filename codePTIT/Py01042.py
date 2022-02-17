from tabnanny import check


test = int(input())
while test>0:
    n = input()
    check = False
    for i in n:
        if i!='0' and i!='1' and i!='2':
            print("NO")
            check = True
            break
    if check == False: print("YES")
    test -=1