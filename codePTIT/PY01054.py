test=int(input())
while test>0:
    number=input()
    tich=1
    for i in number:
        if int(i)!=0: tich*=int(i)
    print(tich)
    test-=1