# 2953 나는 요리사다
import sys
input = sys.stdin.readline

sumList=[]

for _ in range(5):
    lst = list(map(int, input().split()))
    sumList.append(sum(lst))
    

print(sumList.index(max(sumList))+1, end=" ")
print(max(sumList))