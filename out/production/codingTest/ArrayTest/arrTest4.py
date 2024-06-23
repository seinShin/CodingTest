arr=[]
for i in range(10):
    arr.append(str(int(input())%42))

Sarr = set(arr)    # 집합 -> 중복 허용 x
print(len(Sarr))


