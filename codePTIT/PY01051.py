def daoSo(a):
    return "".join(reversed(a))

test=int(input())
while test>0:
    test-=1
    n=input()
    sum=0
    for i in n: sum+=int(i)
    if len(str(sum))==1: print('NO')
    else:
        print('YES') if int(daoSo(str(sum)))==sum else print('NO')