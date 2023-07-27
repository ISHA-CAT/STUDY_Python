import random #난수 발생 함수를 호출
guess_number = random.randint(1, 100) #1-100 사이 정수 난수 생성
print("숫자를 맞혀 보세요. (1 ~ 100)")
users_input = int(input())
while (users_input is not guess_number):
    if users_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    users_input = int(input()) #다시 사용자 입력을 받음
else:
    print("정답입니다.","입력한 숫자는",users_input,"입니다.")