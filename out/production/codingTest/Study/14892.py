# 14891 톱니바퀴
from collections import deque
import sys 

def left(num, way):
    way *= -1
    if num != 0:
        if wheels[num][6] != wheels[num-1][2]:
            left(num-1,way)
            wheels[num-1].rotate(way)
    

def right(num, way):
    way *= -1
    if num != 3:
        if wheels[num][2] != wheels[num+1][6]:
            right(num+1, way)
            wheels[num+1].rotate(way)


#main
input = sys.stdin.readline

wheels=[]

for i in range(1,5):
    wheels.append(deque(list(map(int, input().strip()))))
   
k = int(input())

for i in range(k):
    num, way = map(int, input().split())
    
    # 회전
    left(num-1, way)
    right(num-1, way)
    wheels[num-1].rotate(way)
    
#결과 계산
rst=0
cnt=1

for i in range(len(wheels)):
    if wheels[i][0] == 1:
        rst+=cnt
    cnt*=2
    
print(rst)