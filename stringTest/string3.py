from string import ascii_lowercase  # string모듈에서 소문자 리스트를 만들기위해 import
S=input()

alist= list(ascii_lowercase)

for a in alist:
    if a not in S:
        print(-1, end=' ')
    else:
        for i in range(len(S)):
            if a == S[i]:
                print(i, end=' ')
                break 
