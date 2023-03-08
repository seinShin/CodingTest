dic = {"A+": 4.5, "A0":4.0, "B+": 3.5, "B0":3.0,"C+":2.5, "C0":2.0, "D+":1.5, "D0": 1.0, "F": 0.0}
subjectArr =[]
grade = 0
totalGrade = 0

for i in range(1,21):
    subject, sub_grade, get_grade = map(str, input().split())
    
    #과목명 검사
    if subject in subjectArr:
        break
    else:
        subjectArr.append(subject)
    
    #치훈이의 과목학점* 본인학점
    if get_grade != "P":
        grade += float(sub_grade)
        totalGrade += (float(sub_grade) * dic[get_grade])

print('%.6f' % (totalGrade/grade))
    
        
        
    