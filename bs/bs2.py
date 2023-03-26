import sys
n = int(sys.stdin.readline())
lst=sorted([*map(int, sys.stdin.readline().split())])
m = int(sys.stdin.readline())
lst2=[*map(int, sys.stdin.readline().split())]
dic={}
for i in lst:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1
        
    
def binary_search(value, start, end):
    if start>end:
        return 0
    
    mid = (start+end) //2
    
    if lst[mid] == value:
        return dic.get(value)
    elif lst[mid] > value:
        return binary_search(value, start, mid-1)
    else:
        return binary_search(value, mid+1 ,end )
    
for i in lst2:
    print(binary_search(i, 0, n-1))
    

