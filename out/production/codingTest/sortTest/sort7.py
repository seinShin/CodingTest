import sys
n = str(sys.stdin.readline())
lst=[]
for i in range(len(n)-1):
    lst.append(n[i])

def split(data):
    if len(data) <=1:
        return data
    medium = int(len(data)/2)
    left = split(data[:medium])
    right= split(data[medium:])
    return merge(left,right)

def merge(left,right):
    merged=[]
    l_point,r_point = 0,0
    
    while len(left)>l_point and len(right)>r_point:
        if left[l_point] < right[r_point]:
            merged.append(right[r_point])
            r_point+=1
        else:
            merged.append(left[l_point])
            l_point+=1
    
    while len(left)>l_point:
        merged.append(left[l_point])
        l_point+=1
    
    while len(right)>r_point:
        merged.append(right[r_point])
        r_point+=1
    
    return merged

lst2=split(lst)
str=''
for i in lst2:
    str+=i
print(int(str))