# 4386 별자리 만들기
import math
import sys
from itertools import combinations

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    a = find(x)
    b = find(y)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
star=[]
parent=[i for i in range(n+1)]

for i in range(n):
    x,y= map(str, input().split())
    star.append([x,y,i+1])
    
edge=[]
for com in combinations(star, 2):
    xCost = (float(com[0][0])-float(com[1][0]))**2
    yCost = (float(com[0][1])-float(com[1][1]))**2
    edge.append((math.sqrt(xCost+yCost), com[0][2], com[1][2]))
        
edge.sort()

rst=0
for ed in edge:
    cost, x, y = ed
    if find(x) != find(y):
        union(x,y)
        rst += cost

print(round(rst, 2))
