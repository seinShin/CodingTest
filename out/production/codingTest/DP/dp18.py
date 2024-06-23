import sys

n,k = map(int, input().split())

lst=[[0,0]]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    for j in range(1,k+1):
        w = lst[i][0]
        v = lst[i][1]
        
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v+ knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][k])