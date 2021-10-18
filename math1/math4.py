import math
# A,B,V = map(int, input().split())
# x=1
# while(True):
#     if(V == (A-B)*x):
#         print(x-1)
#         break
#     elif(V < (A-B)*x):
#         print(x)
#         break
#     else:
#         x+=1
# 시간초과

A,B,V = map(int, input().split())

day = math.ceil((V-B)/(A-B))
print(day)
