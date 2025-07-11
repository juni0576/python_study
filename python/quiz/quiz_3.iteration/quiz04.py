num = int(input("10까지 정수를 입력하세요"))
yak = []
for y in range(1,9):
    if num % y ==0:
        yak.append(y)
print(yak)