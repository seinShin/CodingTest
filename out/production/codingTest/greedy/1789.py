# 1789 수들의 합
import sys
input = sys.stdin.readline

n = int(input())
cnt=0
total=0

while True:
    cnt +=1
    total += cnt
    if total > n:
        break
    
print(cnt-1)
    