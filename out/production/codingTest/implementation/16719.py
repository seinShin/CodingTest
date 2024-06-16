    
# 16719 ZOAC
import sys
input =sys.stdin.readline  

arr = list(input().rstrip()) 

result = [""]*len(arr)

def solution(start,arr):
    if not arr:
        return
    minAlpha = min(arr)
    temp = arr.index(minAlpha)
    
    result[start + temp] = minAlpha
    print("".join(result))
    
    solution(start+temp+1,arr[temp+1:]) 
    solution(start,arr[:temp])

solution(0,arr)