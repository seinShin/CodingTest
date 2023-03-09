n,k = map(int, input().split())
lst=[*map(int, input().split())]
lst.sort()
print(lst[-k])