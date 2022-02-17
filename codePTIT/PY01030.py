
import math


a,b = map(int,input().split())
start = 10 ** (b-1)
end = 10 ** b
count = 0
for i in range(start,end):
    if math.gcd(a,i) == 1:
        print(i,end = ' ')
        count +=1
    if count == 10: 
        print()
        count = 0    
