#1부터 20 사이의 숫자를 입력받고
#정답 숫자를 만들어 놓음(random 함수 사용)
#입력이 정답보다 크면 "정답은 더 작습니다" 출력
#입력이 정답보다 작으면 "정답은 더 큽니다" 출력
#입력이 정답이 같으면 "정답입니다" 출력 후 프로그램 종료

import random
answer = random.randint(1,20) #1~20사이의 랜덤한 숫자 1단위
print(answer)

trycount = 0

while(True):
  tryNumber = int(input("정답을 맞춰보세요:"))
  if tryNumber < answer:
    print("입력이 정답보다 작습니다")
  elif tryNumber > answer:
    print("입력이 정답보다 큽니다")
  elif tryNumber == answer:
   print("정답입니다!")
   break
  trycount=trycount+1
  if(trycount>=5):
    print("틀렸습니다.")
    break