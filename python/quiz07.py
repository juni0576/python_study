import math
x1=int(input("첫번째 x좌표"))
y1=int(input("첫번째 y좌표"))
x2=int(input("두번째 x좌표"))
y2=int(input("두번째 y좌표"))

distance = math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2)
print(distance)