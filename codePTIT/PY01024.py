def sum(n):
    res = 0
    for i in n: res += int(i)
    if(res % 10 == 0): return True
    return False

def CheckDV(n):
    for i in range(1,len(n)-1):
        if(abs(int(n[i])-int(n[i+1])) != 2 or abs(int(n[i])-int(n[i-1])) != 2): return False
    return True

test = int(input())
while test>0:
    n = input()
    if sum(n) == True and CheckDV(n) == True: print("YES")
    else: print("NO")
    test -=1