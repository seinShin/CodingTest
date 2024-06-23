import sys
from collections import Counter
lst=[]
n = int(sys.stdin.readline())
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
    
def split(data):
    if len(data)<=1:
        return data
    medium = int(len(data) / 2)
    left = split(data[:medium])
    right = split(data[medium:])
    return merge(left, right)

def merge(left,right):
    merged=[]
    l_point, r_point = 0,0
    
    while len(left) > l_point and len(right) > r_point:
        if left[l_point] > right[r_point]:
            merged.append(right[r_point])
            r_point += 1
        else:
            merged.append(left[l_point])
            l_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > l_point:
        merged.append(left[l_point])
        l_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > r_point:
        merged.append(right[r_point])
        r_point += 1
    
    return merged


def modeFinder(lst):
    c = Counter(lst)
    order = c.most_common()
    maxn=order[0][1]
    
    modes=[]
    for num in order:
        if num[1] == maxn:
            modes.append(num[0])
    
    if len(modes)>1:
        modes2=split(modes)
        return modes2[1]
    else:
        return order[0][0]
            


sorted_list = split(lst)

print(round(sum(lst) / n))
print(sorted_list[len(lst)//2])
print(modeFinder(lst))
print(sorted_list[-1]-sorted_list[0])

