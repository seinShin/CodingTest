import sys
lst=[]
for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))

#퀵정렬 초과
# def qsort(data):
#     if len(data) <= 1:
#         return data
    
#     pivot = data[0]

#     left = [ item for item in data[1:] if pivot > item ]
#     right = [ item for item in data[1:] if pivot <= item ]
    
#     return qsort(left) + [pivot] + qsort(right)
# lst2 = qsort(lst) 

#병합정렬
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

lst2=mergesplit(lst)
for i in lst2:
    print(i)


