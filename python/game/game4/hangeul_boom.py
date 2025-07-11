#한글 폭탄제거 게임
words= [
    "재료공학",
    "탄소강", "합금", "주철", "인장강도", "경도", "연성", "취성", "열처리", "열팽창계수", "피로",
    "열역학",
    "열역학 법칙", "엔탈피", "엔트로피", "내부 에너지", "단열", "등온", "열기관", "냉각기", "열전달", "열교환기",
    "동역학", "운동학",
    "뉴턴의 법칙", "관성", "질량", "가속도", "회전", "토크", "각속도", "운동량", "진동", "감쇠",
    "유체역학",
    "유속", "점도", "레이놀즈 수", "베르누이 방정식", "압력", "유량", "유체저항", "캐비테이션", "터빈", "펌프",
    "설계/제도",
    "CAD", "공차", "치수", "조립도", "해석도", "나사산", "베어링", "기어", "링크", "캠",
    "제어공학",
    "센서", "액추에이터", "피드백", "제어계", "PLC", "PID 제어", "자동화", "로봇공학", "서보 시스템", "마이크로컨트롤러"
]

import random
import time

def display_point():
    return print(f"생명 : {life}\n점수 : {score}\n제한시간 : {limit_time}\n\n")

life = 3
score = 0
limit_time = 3

while life !=0 or score <11:
    ran_word = random.choice(words)
    print(ran_word)
    user_st = time.time()
    user_typing = input("빨리 폭탄을 해체하시오 \n")
    user_end = time.time()
    take_time = user_end - user_st

    if user_typing == ran_word:
        score +=1
        if take_time > limit_time:
            life -=1
            print(f"제한 시간 오버 \n ") 
        display_point()
    else:
        life -=1
        score -=1
        display_point()
