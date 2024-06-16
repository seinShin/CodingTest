# 2002 해시
import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
carDic={}

for i in range(n):
    carDic[input().strip()] = i+1

arr=[]
for i in range(n):
    outCar = input().strip()
    arr.append(outCar)


cnt=0
for i in range(n-1):
    for j in range(i+1, n):
        if carDic[arr[i]] > carDic[arr[j]]:
            cnt+=1
            break
            
        
print(cnt)
    
    
    
