# s = input()
# s1 = s[::-1]
# s2 = s1.split()

# if s2[0]>s2[1]:
#     print(s2[0])
# else:
#     print(s2[1])

a,b = input().split()
print(max(a[::-1], b[::-1]))
