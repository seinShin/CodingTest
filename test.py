from itertools import permutations, combinations

lst = ['A', 'B', 'C']

for i in permutations(lst,2):
    print("순열 :", i)
    
for i in combinations(lst,2):
    print("조합 :", i)