s = input()
arr = []
for i in s:
    if i >= "0" and i <="9": arr.append(i)

if(int(arr[0]) + int(arr[1]) == int(arr[2])): print("YES")
else: print("NO")
