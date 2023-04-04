

n = input().split('-')

num=[]

for i in n:
    cnt=0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)

start = num[0]
for i in range(1, len(num)):
    start -= num[i]

print(start)
