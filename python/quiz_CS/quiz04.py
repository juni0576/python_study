#조건문 4번 문제
import math
r = int(input("원의 반지름을 알려주면 원의 넓이를 구해요"))
if r>0:
    print(math.pi*r**2)
else:
    print("잘못된 값입니다.")