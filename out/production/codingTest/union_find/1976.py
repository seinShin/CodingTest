import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
rst=True

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a 
    else:
        parent[a] = b 
        
for i in range(n):
    cityList = list(map(int, input().split()))
    
    for j in range(len(cityList)):
        city = i+1
        idx = j+1
        if i != j and cityList[j] == 1:
            union(city, idx)

plan = list(map(int, input().split()))

root = parent[plan[0]]
for i in range(len(plan)):
    x=plan[i]
    if root != parent[x]:
        rst = False
        break

if rst == False:
    print("NO")
else:
    print("YES")

    