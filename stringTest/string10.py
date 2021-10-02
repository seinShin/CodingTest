N = int(input())
cnt=0
for i in range(N):
    alpa=input()
    for j in range(len(alpa)):
        if j !=len(alpa)-1:
            if alpa[j] == alpa[j+1]:
                pass
            elif alpa[j] in alpa[j+1:]:
                break
        else:
            cnt+=1
print(cnt)