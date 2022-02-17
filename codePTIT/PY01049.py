import math


def Prime(n):
    if(n<2):return False
    for i in range(2,int(math.sqrt(n)) +1):
        if n % i == 0: return False
    return True

def Check_Count(n):
    prime = 0
    notprime = 0
    for i in n:
        if(Prime(int(i)) == True): prime +=1
        else: notprime +=1
    if(prime > notprime): return True
    return False


test=int(input())
while test>0:
    n=input()
    if Prime(len(n)) == True and Check_Count(n) == True: print("YES")
    else: print("NO")
    test-=1