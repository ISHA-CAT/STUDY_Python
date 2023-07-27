#변수 : user_input, result
#프로그램이 시작되면 ‘구구단 몇 단을 계산할까?’가 출력
#사용자는 계산하고 싶은 구구단 단수를 입력
#프로그램은 ‘구구단 n단을 계산한다.’라는 메시지와 함께 구구단의 결과를 출력

print("구구단 몇 단을 계산할까?")
user_input = int(input())
print("구구단",user_input,"단을 계산한다.")

for i in range(1, 10, 1):
    result = user_input * i
    print(user_input,"x",i,"=",result)