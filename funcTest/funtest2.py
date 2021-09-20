#리스트 이용
numList= list(range(1,10001)) # 10000까지의 전체 숫자
removeList=[] # 삭제할 리스트

for i in numList:
    for n in str(i):
        i += int(n)
    if i <=10000:
        removeList.append(i)

for j in set(removeList):
    numList.remove(j)

for result in numList:
    print(result)


