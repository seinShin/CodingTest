xList =[]
yList =[]

for i in range(3):
    x,y= input().split()
    xList.append(x)
    yList.append(y)

for i in range(3):
    if xList.count(xList[i]) == 1:
        x = xList[i]
    if yList.count(yList[i]) == 1:
        y = yList[i]

print(x,y)