import sys
input = sys.stdin.readline

lst1 = [*map(str, input().strip())]
lst2 = [*map(str, input().strip())]

dp=[[0]* (len(lst2)+1) for _ in range(len(lst1)+1)]


for i in range(1, len(lst1)+1):
    for j in range(1, len(lst2)+1):
        if lst1[i-1] == lst2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            

print(dp[-1][-1])