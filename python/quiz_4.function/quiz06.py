import math
def right_tri_side(x,y):
    return math.sqrt(x**2+y**2)

x=int(input("첫번째 정수"))
y=int(input("두번째 정수"))

print("직각 삼각형의 빗변의 길이는?", right_tri_side(x,y))