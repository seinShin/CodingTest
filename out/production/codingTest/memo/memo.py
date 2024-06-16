test_case = int(input())

for i in range(test_case):
    l = []
    r=[]
    data=input()
    
    for i in data:
        if i=='-':
            if l:
                l.pop()
        elif i =='<':
            if l:
                r.append(l.pop())
        elif i=='>':
            if r:
                l.append(r.pop())
        else:
            l.append(i)
    
    l.extend(reversed(r))
    print(''.join(l))