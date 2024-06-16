#네이버 test
arr=list(map(int, input().split()))
arr.sort()

answer=[]
tmp=arr[0]
cnt=0

for i in range(1,len(arr)):
    if tmp== arr[i]:
        cnt+=1
        if i == len(arr)-1:
            answer.append(cnt+1)
    else:
        if cnt != 0:
            answer.append(cnt+1)
        tmp=arr[i]
        cnt=0

if len(answer) == 0:
    print(-1)
else:
    print(answer)