


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
    check = False
    res = n
    if(res % 7 == 0): 
        print(res)
        check = True
    else:
        for i in range(1000+1):
            res = res + reverse_number(res)
            if res % 7 == 0:
                check = True
                print(res)
                break
    if check == False: print(-1)
    test -=1