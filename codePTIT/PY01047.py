import math


def Prime(n):
    if(n<2):return False
    for i in range(2,int(math.sqrt(n)) +1):
        if n % i == 0: return False
    return True

test=int(input())
while test>0:
    s=input()
    number=''
    for i in range(len(s)-4,len(s)): number+=s[i]
    print('YES') if Prime(int(number)) else print('NO')
    test-=1