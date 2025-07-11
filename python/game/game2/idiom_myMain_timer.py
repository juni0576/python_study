# 속담 맞추기 게임
import random
import time
import threading

idiom = [
    ["가는 날이" , "장날이다"],
    ["가는 말이 고와야","오는 말이 곱다"],
    ["가재는","게 편"],
    ["사공이 믾으면","배가 산으로 간다"],
    ["고양이 목에","방울 달기"],
    ["공든 탑이","무너지랴"],
    ["꿩 대신","닭"],
    ["개천에서","용난다"],
    ["개구리 올챙이 적", "생각 못 한다"],
    ["고기는 씹어야 맛이고,","말은 해야 맛이다"],
    ["낫 놓고","기역자도 모른다"],
    ["누워서", "침 뱉기"],
    ["달면 삼키고", "쓰면 뱉는다"],
    ["도둑이","제 발 저린다"],
    ["등잔 밑이", "어둡다"],
    ["배보다","배꼽이 크다"],
    ["벼룩의 간을","빼먹는다"],
    ["병 주고", "약 준다"],
    ["얌전한 고양이", "부뚜막에 먼저 올라간다"]
]

count = 0
limit_time = 30
game_over = False  # ⛔️ 시간 초과 시 중단 flag

def timeout_flag():
    global game_over
    time.sleep(limit_time)
    game_over = True
    print("\n⏰ 전체 제한시간 초과! 게임이 종료됩니다.\n")

# ⏱ 타이머 쓰레드 시작
timer_thread = threading.Thread(target=timeout_flag)
timer_thread.start()

print("🎮 게임 시작! 제한 시간은 30초입니다.\n")

i = 0
while i < 5 and idiom and not game_over:
    ran_fb = random.choice(idiom)
    idiom.remove(ran_fb)
    ch_ran_fb = ran_fb[random.randint(0, 1)]
    print(f"Q{i+1}: ? {ch_ran_fb} ?")
    try:
        user_ans = input("정답을 입력하세요: ")
    except:
        break  # 입력 중 예외가 발생하면 종료

    if game_over:
        break  # 입력 중 시간이 초과되었으면 즉시 종료

    if user_ans == ran_fb[0] or user_ans == ran_fb[1]:
        print("🎉 정답입니다!\n")
        count += 1
    else:
        print(f"오답입니다! \n 정답은 {ran_fb}\n")
    i += 1

print(f"📊 결과: 총 {i}문제 중 {count}개 정답!")
