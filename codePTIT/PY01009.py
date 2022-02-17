from itertools import count


s = input()
count1 = 0
count2 = 0
for i in s: 
    if i >= 'A' and i <= 'Z': count1 +=1
    else: 
        if i>='a' and i <='z': count2 +=1

if count2 >= count1: print(s.lower())
else: print(s.upper())
