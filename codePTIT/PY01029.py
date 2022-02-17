


import math


def reverse_number(n):
    m = n
    sum = 0
    while m>0:
        tmp = m % 10
        m //=10
        sum = sum * 10 + tmp
    return sum    


test = int(input())
while test>0:
    n =int(input())
    if(math.gcd(n,reverse_number(n)) == 1): print("YES")
    else: print("NO")
    test -=1