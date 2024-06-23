
lst =[1,3,2,7]
lis =[lst[0]]

def binarySearch(x):
    start = 0
    end = len(lis)-1
    
    while start <= end:
        mid = (start+end) //2
        
        if lis[mid] == x:
            return mid
        elif lst[mid] <x:
            start = mid +1
        else:
            end = mid -1
    return start

for i in range(1,len(lst)):
    if lst[i]> lis[-1]:
        lis.append(lst[i])    
    else:
        idx = binarySearch(lst[i])
        lis[idx] = lst[i]
        
            
print(lis)
print(len(lis))	