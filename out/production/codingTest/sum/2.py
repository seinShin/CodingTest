import sys
input = sys.stdin.readline

n,k = map(int, input().split())

lst=[*map(int, input().split())]
psum = sum(lst[:k])
suml=[psum]


for i in range(0,len(lst)-k):
    psum = psum - lst[i] + lst[i+k]
    suml.append(psum)
    
print(max(suml))