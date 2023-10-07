# 2003 수들의 합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst=[*map(int, input().split())]

# cnt=0
# for i in range(len(lst)):
#     temp = 0
#     for j in range(i, len(lst)):
#         temp+=lst[j]
#         if temp == m:
#             cnt+=1
#             break
# print(cnt)
           
sum=lst[0]
left=0
right=1
cnt=0

while True:
    if sum < m:
        if right < n:
            sum+=lst[right]
        else:
            break
    elif sum == m:
        cnt+=1
        sum-=lst[left]
        left+=1
    else:
        sum -=lst[left]
        left+=1
print(cnt)