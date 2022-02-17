
import math


def NT(n):
    if n < 2: return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0: 
                return False
    return True

def coprime(a,b):
    if math.gcd(a,b) == 1: return True
    return False

n = int(input())
while n>0:
    x = int(input())
    count = 0
    for i in range(1,x):
        if coprime(i,x) == True: count +=1   
    if NT(count) == True: print("YES")
    else: print("NO")    
    n-=1
