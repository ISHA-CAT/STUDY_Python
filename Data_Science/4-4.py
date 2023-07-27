#나이는 (2023 - 태어난 년도 + 1)로 계산
#26세 이하 20세 이상이면 ‘대학생’
#20세 미만 17세 이상이면 ‘고등학생’
#17세 미만 14세 이상이면 ‘중학생’
#14세 미만 8세 이상이면 ‘초등학생’
#그 외의 경우는 ‘학생이 아닙니다.’ 출력

# <작성한 코드>
birth_year = int(input("당신이 태어난 연도를 입력하세요"))
age = 2023 - (birth_year) + 1

if age <= 26 and age >= 20: print("대학생")
elif age < 20 and age >= 17: print("고등학생")
elif age < 17 and age >= 14: print("중학생")
elif age < 14 and age >= 8: print("초등학생")
else: print("학생이 아닙니다.")

# <교재 코드>
print("당신이 태어난 연도를 입력하세요.")
birth_year = 2023 - int(birth_year) + 1

if age <= 26 and age >= 20: 
    print("대학생")
elif age < 20 and age >= 17: 
    print("고등학생")
elif age < 17 and age >= 14: 
    print("중학생")
elif age < 14 and age >= 8: 
    print("초등학생")
else: 
    print("학생이 아닙니다.")