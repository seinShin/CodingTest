# 8979 올림픽
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nation=[]
medal=[0]*(n+1)

for _ in range(n):
    lst=list(map(int, input().split()))
    nation.append(lst)
    
nationSorting = sorted(nation, key = lambda x : (-x[1], -x[2], -x[3]))

# print(nationSorting)

rank=1
for i in range(len(nationSorting)-1):
    if medal[nationSorting[i][0]] == 0:
        medal[nationSorting[i][0]] = rank
    else:
        rank+=1
    if nationSorting[i][1] > nationSorting[i+1][1]:
        rank+=1
    elif nationSorting[i][1] == nationSorting[i+1][1]:
        if nationSorting[i][2] > nationSorting[i+1][2]:
            rank+=1
        elif nationSorting[i][2] == nationSorting[i+1][2]:
            if nationSorting[i][3] > nationSorting[i+1][3]:
                rank+=1
            else:
                medal[nationSorting[i+1][0]] = medal[nationSorting[i][0]]
                

for i in range(1,len(medal)):
    if medal[i] == 0:
        medal[i] = rank
        break
# print(medal)
print(medal[k])
        