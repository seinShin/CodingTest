import sys
input = sys.stdin.readline

n = int(input())
lst=[*map(int, input().split())]
m = int(input())
lst2=[*map(int, input().split())]
start, end = 0, len(lst)-1

lst.sort()
def bs(lst, search, start, end):
    if start> end:
        return 0
    
    mid = (start+end) //2
    
    if search == lst[mid]:
        return 1
    else:
        if search >= lst[mid]:
            return bs(lst, search, mid+1, end)
        else:
            return bs(lst, search, start, mid-1)

for i in lst2:
    print(bs(lst, i, start, end), end=' ')    