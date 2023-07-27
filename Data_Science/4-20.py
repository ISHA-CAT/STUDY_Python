print("구구단 몇 단을 계산할까요(1~9)")
x = 1
while(x is not 0):
    x = int(input())
    if (x == 0): break
    if not(0 <= x <= 9):
        print("잘못 입력했습니다. 1부터 9 사이 숫자를 입력해주세요.")
    else:
        print("구구단",x,"단을 계산합니다.")
        for i in range(1, 10):
            print(x,"x",i,"=",(x * i))
        print("구구단 몇 단을 계산할까요?(1~9)")
print("구구단 게임을 종료합니다.") #while문이 끝나면 실행되는 코드