#1148 단어 만들기
import sys 
input = sys.stdin.readline

#test
# words=["APPLE","BANANA","BANE","BRILLIANT","LINT","PALE","PROBLEM","TILL","TRILL"]

# puzzles=["LARBITNLI", "LEPAPBNNA", "LEPAPBNAM"]


#입력
words=[]
while True:
    word = str(input().strip())
    if word == '-':
        break
    words.append(word)
    
puzzles=[]
while True:
    puzzle = str(input().strip())
    if puzzle == '#':
        break
    puzzles.append(puzzle)

#문자열 생성 가능성 체크 함수
def check(word, puzzle):
    for alpa in word:
        if word.count(alpa) > puzzle.count(alpa):
            return False
    return True
    
#main
for puzzle in puzzles:
    # 단어 딕셔너리
    wordDic = {}
    
    for p in puzzle:
        wordDic[p] = 0
        for word in words:
             # 정중앙 체크 -> 문자열 생성 가능성 체크
            flag = True
            if p in word:
                flag=check(word, puzzle)
                if flag:
                    wordDic[p] += 1
                    
    #출력
    minList=[]
    maxList=[]
    
    for alpa in wordDic:
        if wordDic[alpa] == min(wordDic.values()):
              minList.append(alpa)
        if wordDic[alpa] == max(wordDic.values()):
            maxList.append(alpa)
    minNum = min(wordDic.values())
    maxNum = max(wordDic.values())
    
    #정렬 후 출력
    minList.sort()
    maxList.sort()
    
    print("".join(minList), minNum, end=' ')
    print("".join(maxList), maxNum)    
    
    
    
        
                    
        
        
    