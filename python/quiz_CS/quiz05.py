#조건문 5번 문제
num1 = int(input("정수1"))
num2 = int(input("정수2"))
num3 = int(input("정수3"))

if num1<num2 and num1<num3:
    print(f"num1({num1})이 제일 작다.")
elif num2<num1 and num2<num3:
    print(f"num2({num2})이 제일 작다.")
else :
    print(f"num3({num3})이 제일 작다.")