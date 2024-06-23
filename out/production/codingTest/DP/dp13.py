import sys

input = sys.stdin.readline

n = int(input())
lst=[*map(int, input().split())]
dp1=[1]*n
dp2=[1]*n

for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

re_lst=lst[::-1]

for i in range(n):
    for j in range(i):
        if re_lst[i]>re_lst[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
            
dp2.reverse()

rst=[]
for i in range(n):
    rst.append(dp1[i]+dp2[i])
print(max(rst)-1)