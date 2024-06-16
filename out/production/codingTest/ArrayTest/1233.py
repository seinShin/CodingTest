# 1233 주사위
import sys
input = sys.stdin.readline

s1,s2,s3 = map(int, input().split())

dic={}
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            tmp = i+k+j
            if tmp not in dic:
                dic[tmp] = 1
            else:
                dic[tmp] += 1
          
max = -1 
answer= 81
for (key, value) in dic.items():
    if max < value:
        max = value
        answer = key
    elif max == value:
        answer = min(answer, key)
        
print(answer)


        
    