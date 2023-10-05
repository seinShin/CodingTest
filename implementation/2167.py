# 2167 2차원 배열의 합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
DP = [[0 for i in range(0, m+1)] for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, m+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + lst[i-1][j-1]
 
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])
    