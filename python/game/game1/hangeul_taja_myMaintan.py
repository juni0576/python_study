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
user_typing = input(f"'{ran_sen}' 를 빨리 따라서 쓰시오.")
user_end = time.time()
used_time = user_end-user_st


correct =0
for i in range(min(len(ran_sen),len(user_typing))):
    if ran_sen[i]==user_typing[i]:
        correct+=1
            
total = max(len(ran_sen),len(user_typing))
accuracy = (correct/total)*100
speed = len(user_typing)/used_time *60

def until_no_error(a):
        if a != 100:
            return "정확하게 치세요"
        return "정확합니다!"
n=0
while until_no_error(accuracy) != "정확합니다!":
    print(until_no_error(accuracy))
    user_typing = input(f"'{ran_sen}' 를 다시 따라서 쓰시오.")
    
    correct =0
    for i in range(min(len(ran_sen),len(user_typing))):
        if ran_sen[i]==user_typing[i]:
            correct+=1
    total = max(len(ran_sen),len(user_typing))
    accuracy = (correct/total)*100
    speed = len(user_typing)/used_time *60
    
    n+=1

print("\n결과")
print(f"걸린 시간: {round(used_time,3)}초")
# print(f"정확도: {accuracy}%")
print(f"타자 속도: {round(speed,3)} CPM")
print(f"재시도 횟수: {n}")

