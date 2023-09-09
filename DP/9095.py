# 9095 1,2,3 더하기
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    
    dp=[0]*11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for k in range(4, n+1):
        dp[k] = dp[k-1]+dp[k-2]+dp[k-3]
    print(dp[n])