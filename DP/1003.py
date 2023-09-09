# 1003 피보나치 함수
import sys
input = sys.stdin.readline
  
    
t = int(input())

for i in range(t):
    zeroCnt=[1,0]
    oneCnt=[0,1]
    
    n = int(input())

    for _ in range(2, n+1):
        zeroCnt.append(oneCnt[-1])
        oneCnt.append(oneCnt[-1]+ zeroCnt[-2])
        
    print(zeroCnt[n], oneCnt[n])