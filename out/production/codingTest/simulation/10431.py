# 10431 줄세우기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    arr=[*map(int, input().split())]

    
    chk=0
    for i in range(1,len(arr)-1):
        for j in range(i+1, 1, -1):
            if arr[j] < arr[j-1]:
                chk +=1
                arr[j], arr[j-1] = arr[j-1], arr[j]  
            

    print(arr[0], chk)