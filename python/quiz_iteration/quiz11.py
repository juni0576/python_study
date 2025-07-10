num1 = int(input("정수1"))
num2 = int(input("정수2"))

yak1 = []
yak2 = []
max_yak =[]
for x in range(1, num1+1):
    if num1%x==0:
        yak1.append(x)
for y in range(1,num2+1):
    if num2%y ==0:
        yak2.append(y)
print(yak1,yak2)

for xx in yak1:
    for yy in yak2:
        if xx==yy:
            max_yak.append(xx)

print(max(max_yak))