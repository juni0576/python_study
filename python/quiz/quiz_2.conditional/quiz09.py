#조건문 9번 문제
import random
num1=random.randint(1,1000)
num2=random.randint(1,1000)

cal=random.randint(0,3) #이게 관건이었는데, 이사님이 보여줘서 알아버림;;

if cal==0:
    Que = num1+num2
    print(f"{num1}+{num2}=?")
    ans = int(input("답을 적으세요!"))

    if Que==ans:
        print("정답!")
    else:
        print("땡 탈락")

elif cal==1:
    Que=num1-num2
    print(f"{num1}-{num2}=?")
    ans = int(input("답을 적으세요!"))

    if Que==ans:
        print("정답!")
    else:
        print("땡 탈락")

elif cal==2:
    Que = num1*num2
    print(f"{num1}x{num2}=?")
    ans = int(input("답을 적으세요!"))

    if Que==ans:
        print("정답!")
    else:
        print("땡 탈락")

else:
    Que = num1/num2
    que = round(Que, 2)
    print(f"{num1}/{num2}=?")
    ans = float(input("답을 적으세요! 소수점이 필요하다면 소수점 2자리까지"))

    if que==ans:
        print("정답!")
    else:
        print("땡 탈락")