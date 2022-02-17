
test = int(input())
while test>0:
    s = input()
    temp = ""
    res = 999999999999999999
    for i in s:
        if i >= "a" and i <= "z":
            if temp != "":
                count = 0
                for j in temp: count  = count * 10 + int(j)
                if count < res: res = count
            temp = ""
        else : temp += i
    print(res)
    test -=1    

