import sys
input = sys.stdin.readline
n_list={}

for i in range(int(input())):
    name,log=map(str, input().split())
    
    if log =='enter':
        n_list[name] = log
    else:
        del n_list[name]
        
sort_list=sorted(n_list.keys(), reverse=True)
for i in sort_list:
    print(i)
