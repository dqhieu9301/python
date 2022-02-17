
input = input()
count1 = 0
count2 = 0
for i in input:
    if i == "4": count1 +=1
    else:
        if i == "7": count2 +=1

if(count2 + count1 == 4 or count2 + count1 == 7): print("YES")
else: print("NO")

