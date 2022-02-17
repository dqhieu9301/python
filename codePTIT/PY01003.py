
import math


test = int(input())
while test>0:
    n = int(input())
    if(n < 10): print(n)
    else :
        count = 0
        while n>9:
            m = n % 10
            n /=10
            if(m < 5): 
                n = math.floor(n)
            else:
                n = math.ceil(n)
            count += 1
        print(int(n * math.pow(10,count)))        

    test -=1