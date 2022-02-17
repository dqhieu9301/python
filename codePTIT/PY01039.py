def check_beauty(n):
    for i in range(len(n)-2):
        if n[i]!=n[i+2]: return False
    return True

test = int(input())
while test>0:
    n = str(input())
    if(check_beauty(n) == True): print("YES")
    else: print("NO")
    test -=1