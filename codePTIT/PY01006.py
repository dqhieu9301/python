
from tokenize import String


def NumberLucky(n):
    for i in n:
        if i != "4" and  i!="7": return False
    return True

x = int(input())
while x>0:
    n = str(input())
    if(NumberLucky(n) == True): print("YES")
    else: print("NO")
    x -=1
