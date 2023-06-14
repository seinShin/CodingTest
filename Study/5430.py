# 5430 AC
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
    r=0
    flag=0
    for i in p:
        # 짝수면 원래 배열, 홀수면 뒤집기
        if i == 'R':
           r +=1
        else:
            if i == 'D':
                #d인데 0이면 error
                if len(lst)==0:
                    flag=1
                    print('error')
                    break
                else:
                    if r %2 == 0:
                        lst.popleft()     
                    else:
                        lst.pop()
    
    if flag != 1:
        if r %2 != 0:
            lst.reverse()
        print('[', end='')
        print(*lst,sep=',', end='')
        print(']')