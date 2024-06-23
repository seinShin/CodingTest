# 15482 한글 LCS

n1=list(input())
n2=list(input())

lcs=[[0 for _ in range(len(n1)+1)] for _ in range(len(n2)+1)]

for i in range(1, len(n2)+1):
    for j in range(1, len(n1)+1):
        if n2[i-1] == n1[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
        
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])