from tokenize import Double


test = int(input())
while test>0:
    s = [float(x) for x in input().split()]
    n = s[0]
    x = s[1]
    m = s[2]
    count = 0
    while True:
        n = n + n *(x/100)
        count +=1
        if n >= m: break
    print(count)    
    test -=1    
