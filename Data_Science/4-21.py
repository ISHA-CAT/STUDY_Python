kor_score = [49, 80, 20, 100, 80] #과목별 점수에 대한 리스트 생성
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midterm_score = [kor_score, math_score, eng_score] #변수에 과목별 점수가 저장되는 리스트 생성

student_score = [0, 0, 0, 0, 0] #학생별로 평균을 구해야 하므로 각 값을 저장할 수 있는 공간인 student_score 리스트를 생성하고 초기화
i = 0 #학생 인덱스를 초기화
for subject in midterm_score: #midterm_score만큼 subject를 반복? -> 과목당 점수를 반복?
    for score in midterm_score: #midterm_score만큼 score를 반복? -> 학생당 점수를 반복
        student_score[i] += score #해당 과목 점수를 기존 student_score[i]에 계속 추가
        i += 1 #학생 인덱스 구분
    i = 0 #과목이 바뀔 때마다 학생 인덱스 초기화
else: #반복문이 모두 끝나면 else문 활성화 -> 3으로 나누어 개인별 성적 출력
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3] #student_average 변수에 학생별 평균 저장
    print(student_average) #학생별 평균 출력