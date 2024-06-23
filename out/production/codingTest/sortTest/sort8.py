import sys

n =int(sys.stdin.readline())
lst = list(map(int, input().split())) 
    
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
        if left[l_point] > right[r_point]:
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

sorted_list = split(list(set(lst)))
dic ={sorted_list[i]:i for i in range(len(sorted_list))}
for i in lst:
    print(dic[i], end=' ')


