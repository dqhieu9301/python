                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
from operator import le
from queue import LifoQueue
from typing import Deque


length = int(input())   
arr = [int(x) for x in input().split()]   
q = LifoQueue()
for i in range(len(arr)):
    q.put(arr[i])  
    if(q.qsize() >= 2): 
        x = q.get()
        y = q.get()
        if (x+y) % 2 == 0: continue
        else :
            q.put(y)
            q.put(x)
print(q.qsize())            
                                                                                                                                       