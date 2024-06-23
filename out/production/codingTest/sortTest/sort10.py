import sys
lst=[]
for i in range(int(sys.stdin.readline())):
    lst.append(list(map(int,input().split())))

def split(data):
    if len(data) <=1:
        return data
    medium = int(len(data)/2)
    left,right=list(),list()
    for i in range(medium):
        left.append(data[i])
    for i in range(medium,len(data)):
        right.append(data[i])
    left = split(left)
    right = split(right)
    
    return merge(left, right)

def merge(left,right):
    merged=[]
    l_point, r_point = 0,0
    while len(left)>l_point and len(right) > r_point:
        if left[l_point][1] > right[r_point][1]:
            merged.append(right[r_point])
            r_point +=1
        elif left[l_point][1] == right[r_point][1]:
            if left[l_point][0] > right[r_point][0]:
                merged.append(right[r_point])
                r_point+=1
            else:
                merged.append(left[l_point])
                l_point+=1
        else:
            merged.append(left[l_point])
            l_point +=1
    
    while len(left)>l_point:
        merged.append(left[l_point])
        l_point+=1
        
    while len(right) > r_point:
        merged.append(right[r_point])
        r_point+=1
        
    return merged

lst2=split(lst)
for i in range(len(lst2)):
    print(lst2[i][0], lst2[i][1])
