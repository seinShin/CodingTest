arr = [[0 for _ in range(101)] for _ in range(101)]

n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0

for i in arr:
    result += i.count(1)
print(result)    
    