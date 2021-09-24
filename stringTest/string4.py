S = int(input())

for i in range(S):
    num,st = input().split()
    for a in st:
       print(a*int(num), end='')
    print()