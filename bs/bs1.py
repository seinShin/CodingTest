import sys

n = int(sys.stdin.readline())
lst = [*map(int, sys.stdin.readline().split())]
m = int(sys.stdin.readline())
lst2 = [*map(int, sys.stdin.readline().split())]
    

lst.sort()
lst.sort()
def binary_search(data, search):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        if data[0] == search:
            return 1
        else:
            return 0
    
    medium = len(data) // 2
    if search == data[medium]:
        return 1
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)
        
for item in lst2:
    print(binary_search(lst2, item))        