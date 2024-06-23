# 1475 방번호
import sys
input = sys.stdin.readline

n = str(input().strip())

dic={}
for i in range(10):
    dic[i]=0

total=0
for i in n:
    if int(i) == 9 or int(i) == 6:
        v1 = dic[6]
        v2 = dic[9]
        if v1 < v2:
            dic[6]+=1
        else:
            dic[9]+=1
    else:
        dic[int(i)] +=1
        
all=dic.values()
maxV = max(all)
print(maxV)