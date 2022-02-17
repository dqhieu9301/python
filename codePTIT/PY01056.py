
import math


def Songuyento(a):
    if a<2: return False
    i = 2
    while i <= math.sqrt(a):
        if a%i==0:
            return False
        i+=1
    return True

test=int(input())
while test>0:
    test-=1
    number=input()
    check=1
    sum=0
    for i in range(0,len(number),2):
        if int(number[i])%2!=0:
            print('NO')
            check=0
            break
        else: sum+=int(number[i])
    if check==1:
        for i in range(1,len(number),2):
            if int(number[i])%2==0:
                print('NO')
                check=0
                break
            else: sum+=int(number[i])
    if check==1 and Songuyento(sum): print('YES')