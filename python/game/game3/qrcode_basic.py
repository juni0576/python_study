# 속담 맞추기 게임 +qr
import random
import qrcode
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

count=0
i=0
def qr(answer):
    img = qrcode.make(answer)
    img.show("정답")

while True:
    ran_fb = random.choice(idiom)
    user_ans = input(f"? {ran_fb[random.randint(0,1)]} ? \n")

    if ran_fb[0] == user_ans or ran_fb[1] == user_ans:
        count+=1
        print("정답입니다\n")
        qr(ran_fb)
    else:
        print("틀렸습니다.\n")
    i+=1
    idiom.remove(ran_fb) #중복 제거

    pause = input ("멈추고 싶어요?  y / n \n")
    if pause =="y" or pause == "Y":
        print("멈춥니다.\n")
        break


print(f"{i}문제 중 {count}개 맞췄습니다")
