import sys
n = int(sys.stdin.readline())
lst=[*map(int, sys.stdin.readline().split())]
dp =[0]*len(lst)

for i in range(n):
    for j in range(i):
        if lst[i]>lst[j] and dp[j]>dp[i]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))