
test = int(input())
while test>0:
    n = input()
    res = ""
    tmp = ""
    for i in n:
        if i >= "A" and i <= "Z":
            tmp += i
        else:
            num = int(i)
            while num >0:
                res += tmp
                num -=1
            tmp = ""
    print(res)    
    test -=1