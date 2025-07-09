#조건문 8번 문제
h=float(input("키는요?"))
w=float(input("몸무게는요?"))
std_w=(h-100)*0.9
if w>std_w:
    print("과체중이세요")
elif w==std_w:
    print("딱 표준체중이세요")
else:
    print("저체중이세요")