import sys
lst=[]

for i in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline().strip())
  
lst = list(set(lst))  
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)