# st = [i for i in range(1,31)]

# for _ in range(28):
#     x = int(input())
#     st.remove(x)

# print(min(x))
# print(max(x))

lst=[0]*30
for i in range(0,28):
    a = int(input())
    lst[a-1] = 1
index=0
for j in lst:
    index+=1
    if j ==0:
        print(index)