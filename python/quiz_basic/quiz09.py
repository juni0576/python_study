num = input("4자리 정수를 입력하시오")
ln=list(num)
for i in range(len(ln)):
    ln[i] = int(ln[i])
print("각 자리수의 합은", sum(ln))
