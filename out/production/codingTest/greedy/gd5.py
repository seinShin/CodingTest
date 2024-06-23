n = int(input())
km=[*map(int, input().split())]
city=[*map(int, input().split())]

total = 0

for i in range(len(city)-1):
    if city[i] <= city[i+1]:
        city[i+1] = city[i]
    total+=(city[i]*km[i])

print(total)