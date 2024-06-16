# 21921 블로그
import sys
input = sys.stdin.readline

n,x = map(int, input().split())
blog = [*map(int, input().split())]

max=0
cnt=0
idx=0
tmp=0

for i in range(n):
    tmp += blog[i]
    if i == x-1:
        max = tmp
    if i>=x:
        tmp-=blog[idx]
        if max<tmp:
            max = tmp
            cnt=0
            
        elif max == tmp:
            cnt+=1
        idx+=1

if max == 0:
    print("SAD")
else:
    print(max)    
    print(cnt+1)