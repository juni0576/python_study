F= float(input("온도를 화씨로 입력하세요"))
F2CC = (F - 32) * 5 / 9
message = "화씨 %.2f도를 섭씨로 바꾸면 %.2f도임"
print(message % (F, F2CC))