
test = int(input())
while test>0:
    n = input()
    n += " "
    count = 0
    res = ""
    for i in range(len(n)-1):
        if n[i] == n[i+1]: count +=1
        else:
            if n[i] == " ": break
            else:
                count +=1
                res += str(count) + n[i]
                count = 0
    print(res)        
    test -=1