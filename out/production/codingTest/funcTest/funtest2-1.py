#집합 이용
numList=set(range(1,10001))
selfset=set()  #생성자

for num in numList:
    for i in str(num):
        num +=int(i)
    if num <= 10000:
        selfset.add(num)

numList=numList-selfset
for num in sorted(numList):
    print(num)
