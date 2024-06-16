# n = int(input())
# lst=[0]*10000000
# if 1<=n and n<=10000000:
#     for i in range(n):
#         lst.append(int(input()))

#     lst.sort()
#     for i in range(len(lst)):
#         print(lst[i])

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)