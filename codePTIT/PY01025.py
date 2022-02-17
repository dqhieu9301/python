n = input()
count = 0
res = ""
i = len(n)-1
while i >= 0:
    count +=1
    if count == 3: 
        if(i == 0): res = n[i] + res
        else:
            res = n[i] + res
            res = "," + res
            count = 0
    else:
        res = n[i] + res
    i -=1
print(res)       
