#1. [Enter your score : ] 라고 물어보고 입력된 값을 정수로 score 변수에 할당
#2. score가 90 이상이면 A, 80 이상이면 B, 70 이상이면 C, 60 이상이면 D, 60 이하면 F
#3. 입력된 값에 따라 조건에 맞는 grade 출력

score = int(input("Enter your score : 98"))
if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'
print(grade)
