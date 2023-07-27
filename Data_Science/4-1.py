#1. Tell me your age? 출력
#2. myage 변수에 정수로 된 값을 입력 받기
#3. myage가 30 미만인 경우, Welcome to the Club. 출력
#4. 그 외의 경우, Oh! No. You are not accepted. 출력

print("Tell me your age?")
myage = int(input())
if myage > 30:
    print("Welcome to the Club.")
else:
    print("Oh! No. You are not accepted.")