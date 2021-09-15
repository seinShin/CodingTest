a=[]
for i in range(9):
    a.append(int(input()))  # 개행으로 여러개 입력 시

print(max(a))
print(a.index(max(a))+1)