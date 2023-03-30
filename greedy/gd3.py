import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))
    
lst.sort(key = lambda x: (x[1], x[0]))

cnt_list=[]
cnt=1
end_time = lst[0][1]
for i in range(1,n):
    if lst[i][0] >= end_time:
        cnt +=1
        end_time = lst[i][1]
        
print(cnt)
    
        
        