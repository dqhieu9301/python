import math


def NT(n):
    if n < 2: return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0: 
                return False
    return True

def coprime(a,b):
    return math.gcd(a,b)

def sum(m):
    Tong = 0
    n = m
    while(n>0):
        x = n % 10
        n = int(n/10)
        Tong += x
    return Tong

test = int(input())
while test>0:
    s = [int(x) for x in input().split()]
    a = s[0]
    b = s[1]
    gcd = coprime(a,b)
    tmp = sum(gcd)
    if NT(tmp) == True: print("YES")
    else: print("NO")
    test -=1
