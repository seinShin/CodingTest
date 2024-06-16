import collections
alpa = input()
alpax = alpa.upper()

ans = collections.Counter(alpax)
max = -1;
for i in ans:
    if ans[i] > max:
        max = ans[i]
        maxletter = i
    elif ans[i] == max:
        maxletter = '?'

print(maxletter)