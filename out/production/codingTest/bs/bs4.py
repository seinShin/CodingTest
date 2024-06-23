n,m = map(int, input().split())
lst=[*map(int, input().split())]
start, end = 1, max(lst)

while start<=end:
    mid = (start+end)//2
    len=0
    
    for i in lst:
        if i> mid:
            len += (i-mid)
        if len> m:
            break
            
    if len >= m:
        start = mid+1
    else:
        end=mid-1

print(end)