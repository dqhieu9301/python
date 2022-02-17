test = int(input())
while test>0:
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if(sum % 3 == 0): print("YES")
    else: print("NO")  
    test -=1