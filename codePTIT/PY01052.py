import math


def prime(a):
    if a<2:
        return False
    i=2
    while i<math.sqrt(a):
        if a%i==0: 
            return False
        i+=1
    return True

test=int(input())
while test>0:
    test-=1
    number=input()
    sum=0
    for i in number: sum+=int(i)
    print('YES') if prime(sum) else print('NO')