#조건문 3번 문제
shape = input("R,T,C 택1 추천")
if (shape == 'r') or (shape=='R'):
    print("Rectangle")
elif (shape == 't') or (shape=='T'):
    print("Triangle")
elif (shape == 'c') or (shape=='C'):
    print("Circle")
else:
    print("Unknown")