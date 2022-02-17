test=int(input())
while test>0:
    n=input()
    if len(n)%2==0: print('NO')
    else:
        if n[0]==n[1]: print('NO')
        else:
            check=True
            for i in range(0,len(n)-1,2):
                if n[i]!=n[i+2]:
                    check=False
                    print('NO',2)
                    break
            if check==True: print('YES')
    test-=1