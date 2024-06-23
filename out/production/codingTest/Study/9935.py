# 9935 문자열 폭발 
import sys
input = sys.stdin.readline

strList = input().strip()
explode = input().strip()
size=len(explode)
temp=[]

for i in strList:
    temp.append(i)    
    if explode ==''.join(temp[-size:]):
        for _ in range(size):
            temp.pop()
                    
if len(temp) != 0:
    print(''.join(temp))
else:
    print("FRULA")