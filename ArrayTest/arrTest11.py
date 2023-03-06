n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
    
for i in range(m):
    i,j = map(int, input().split())
    lst2 = lst[i-1:j]
    lst2.reverse()
    cnt=0
    for i in range(i-1,j):
        lst[i] = lst2[cnt]
        cnt+=1
        
# lst = lst[0:i-1]+arr[i-1:j][::-1]+arr[j:]
print(*lst)