import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    
    p = input()
    n = int(input())
    
    lst = str(input())
    
    if n != 0:
        lst=deque(lst[1:-2].split(','))
    else:
        lst=deque([])
    rev=0
    flag=0
    for i in p:
        if i == 'R':
           rev +=1
        else:
            if i == 'D':
                if len(lst)==0:
                    flag=1
                    print('error')
                    break
                else:
                    if rev %2 == 0:
                        lst.popleft()     
                    else:
                        lst.pop()
    
    if flag != 1:
        if rev %2 != 0:
            lst.reverse()
        print('[', end='')
        print(*lst,sep=',', end='')
        print(']')