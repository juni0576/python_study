import random
import time
sen=[
    "아기 상어 뚜루루 뚜루",
    "귀여운 뚜루루 뚜루",
    "바닷속 뚜루루 뚜루",
    "아기 상어!",
    "엄마 상어 뚜루루 뚜루",
    "어여쁜 뚜루루 뚜루",
    "엄마 상어!",
    "아빠 상어 뚜루루 뚜루",
    "힘이 센 뚜루루 뚜루",
    "바닷속 뚜루루 뚜루",
    "아빠 상어!",
    "할머니 상어 뚜루루 뚜루",
    "자상한 뚜루루 뚜루",
    "할머니 상어!",
    "할아버지 상어 뚜루루 뚜루",
    "멋있는 뚜루루 뚜루",
    "할아버지 상어!",
    "우리는 뚜루루 뚜루",
    "바다의 뚜루루 뚜루",
    "사냥꾼 뚜루루 뚜루",
    "상어 가족!",
    "상어다 뚜루루 뚜루",
    "도망쳐 뚜루루 뚜루",
    "숨자!! 으악!",
    "살았다 뚜루루 뚜루",
    "살았다",
    "신난다 뚜루루 뚜루",
    "춤을 춰 뚜루루 뚜루",
    "노래 끝",
    "오예!"
]
ran_sen = random.choice(sen)
print(ran_sen)

user_st = time.time()
trial=1
while True:
    user_typing = input(f"'{ran_sen}' 를 빨리 따라서 쓰시오.")
    user_end = time.time()
    used_time = user_end-user_st

    correct =0
    for i in range(min(len(ran_sen),len(user_typing))):
        if ran_sen[i]==user_typing[i]:
            correct+=1

    total = max(len(ran_sen),len(user_typing)) 
    #버그 고침. 이렇게 안하면, ran_sen까지 정확히 치고 그 뒤로 아무렇게나 쳐도 정확도가 100%나왔음
    accuracy = (correct/total)*100
    speed = len(user_typing)/used_time *60
    if accuracy == 100:
        print("완료했어요")
        break
    else :
        print("다시 시도해보세요")
        trial +=1

print("\n결과")
print(f"걸린 시간: {round(used_time,3)}초")
print(f"시도횟수: {trial}")
print(f"타자 속도: {round(speed,3)} CPM")