import math


def NT(n):
    if n < 2: return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0: 
                return False
    return True

test = int(input())
while test>0:
    n = input()
    test -=1