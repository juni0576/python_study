#조건문 6번 문제
import random
com = random.randint(1,3)
User = int(input("가위바위보 \n 가위 : 1 바위 : 2 보 : 3"))

if com == 1:
    if User == 1:
        print("비겼다")
    elif User == 2:
        print("이겼다")
    else:
        print("졌다")
elif com == 2:
    if User == 1:
        print("졌다")
    elif User == 2:
        print("비겼다")
    else:
        print("이겼다")
else:
    if User == 1:
        print("이겼다")
    elif User == 2:
        print("졌다")
    else:
        print("비겼다")